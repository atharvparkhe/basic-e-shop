from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from app.models import ProductModel
from .serializers import *
from .threads import *
from .models import *
from decouple import config
import razorpay

client = razorpay.Client(auth=(config("PUBLIC_KEY"), config("PRIVATE_KEY")))


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def buy_now(request):
    try:
        data = request.data
        customer = CustomerModel.objects.get(email=request.user.email)
        serializer = ModifyCartItemsSerializer(data=data)
        if serializer.is_valid():
            product_obj = ProductModel.objects.get(id=serializer.data["product_id"])
            cart_obj, _ = OrderModel.objects.get_or_create(owner=customer, is_paid=False)
            if cart_obj.related_cart.filter(item=product_obj).exists():
                cart_item = OrderItemsModel.objects.get(cart=cart_obj, item=product_obj)
                if serializer.data["quantity"]:
                    cart_item.quantity += serializer.data["quantity"]
                    cart_item.save()
                else:
                    cart_item.quantity += 1
                    cart_item.save()
            else :
                if serializer.data["quantity"]:
                    OrderItemsModel.objects.create(owner=customer ,cart=cart_obj, item=product_obj, quantity=int(serializer.data["quantity"]))
                else:
                    OrderItemsModel.objects.create(owner=customer ,cart=cart_obj, item=product_obj)
            ser = OrderItemSerializer(cart_obj.related_cart.all(), many=True)
            return Response({"data":ser.data, "message":"item added to cart"}, status=status.HTTP_202_ACCEPTED)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def apply_coupon(request):
    try:
        data = request.data
        customer = CustomerModel.objects.get(email=request.user)
        serializer = CouponSerializer(data=data)
        if serializer.is_valid():
            cart_obj = OrderModel.objects.get(owner=customer)
            if not cart_obj:
                return Response({"message":"Cart does not exist"}, status=status.HTTP_403_FORBIDDEN)
            if CouponsModel.objects.filter(coupon_name=serializer.data["coupon_code"]).exists() and cart_obj.coupon_applied == False:
                coupon_obj = CouponsModel.objects.get(coupon_name = serializer.data["coupon_code"])
                cart_obj.total_amt -= cart_obj.total_amt*coupon_obj.coupon_discount_amount
                cart_obj.coupon_applied = True
                cart_obj.save()
                coupon_obj.save()
                return Response({"message":"Coupon Applied"}, status=status.HTTP_202_ACCEPTED)
            return Response({"message":"invalid coupon code"}, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def checkout(request):
    try:
        user = CustomerModel.objects.get(email=request.user.email)
        if not OrderModel.objects.filter(owner=user, is_paid=False).exists():
            return Response({"message":"No items exist in cart"}, status=status.HTTP_404_NOT_FOUND)
        cart_obj = OrderModel.objects.get(owner=user, is_paid=False)
        payment = client.order.create({
            'amount' :  cart_obj.total_amt * 100,
            'currency' : 'INR',
            'payment_capture' : 1 
        })
        if cart_obj.razorpay_order_id == None:
            cart_obj.razorpay_order_id = payment["id"]
            cart_obj.save()
        serializer = OrderSerializer(cart_obj)
        return Response({"cart":serializer.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def resultPage(request):
    try:
        data = request.data
        user = CustomerModel.objects.get(email=request.user.email)
        cart_obj = OrderModel.objects.get(owner=user, is_paid=False)
        serializer = PaymentCredentials(data=data)
        if serializer.is_valid():
            payment_credentials = {
                "razorpay_order_id" : cart_obj.order_id,
                "razorpay_payment_id" : serializer.data["payment_id"],
                "razorpay_signature" : serializer.data["signature"]
            }
            check = client.utility.verify_payment_signature(payment_credentials)
            if check:
                return Response({"message":"Payment Failed"}, status=status.HTTP_403_FORBIDDEN)
            cart_obj.payment_id = payment_credentials["razorpay_payment_id"]
            cart_obj.payment_signature = payment_credentials["razorpay_signature"]
            cart_obj.is_paid = True
            thread_obj = generate_invoice(cart_obj)
            thread_obj.start()
            cart_obj.save()
            return Response({"message":"Payment Successfull"}, status=status.HTTP_200_OK)
        return Response({"error":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


