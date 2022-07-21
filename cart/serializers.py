from rest_framework import serializers
from authentication.serializers import CustomerDetailsSerializer
from app.serializers import AllProductsSerializer
from .models import *


class OrderItemSerializer(serializers.ModelSerializer):
    item = AllProductsSerializer()
    class Meta:
        model = OrderItemsModel
        fields = ["item", "quantity", "total"]


class OrderSerializer(serializers.ModelSerializer):
    cart_items = serializers.SerializerMethodField()
    owner = CustomerDetailsSerializer()
    class Meta:
        model = OrderModel
        exclude = ["created_at", "updated_at", "is_paid", "razorpay_payment_id", "razorpay_signature", "cancellation_request"]
    def get_cart_items(self, obj):
        cart_items = []
        try:
            cart_obj = OrderModel.objects.get(id = obj.id)
            serializer = OrderItemSerializer(cart_obj.related_cart.all(), many=True)
            cart_items = serializer.data
            return cart_items
        except Exception as e:
            print(e)


class PaymentCredentials(serializers.Serializer):
    razorpay_payment_id  = serializers.CharField(required = False)
    razorpay_signature  = serializers.CharField(required = False)


class CouponSerializer(serializers.Serializer):
    coupon_code = serializers.CharField(required = True)


class ModifyCartItemsSerializer(serializers.Serializer):
    product_id = serializers.CharField(required = True)
    quantity = serializers.IntegerField(required = True)


# class OrderAll(serializers.ModelSerializer):
#     cart_items = serializers.SerializerMethodField()
#     owner = CustomerDetailsSerializer()
#     class Meta:
#         model = OrderModel
#         fields = "__all__"
#     def get_cart_items(self, obj):
#         cart_items = []
#         try:
#             cart_obj = OrderModel.objects.get(id = obj.id)
#             serializer = OrderItemSerializer(cart_obj.related_cart.all(), many=True)
#             cart_items = serializer.data
#             return cart_items
#         except Exception as e:
#             print(e)