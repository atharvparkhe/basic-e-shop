from django.db import models
from authentication.models import CustomerModel
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from base.models import BaseModel
from app.models import ProductModel
from django.db.models import Sum

Order_Staus = (("pending","Pending"),("packed","Packed"),("dispatched","Dispatched"),("transit","In Transit"),("out","Out For Delivery"),("delivered","Delivered"),("cancelled","Cancelled"))


class OrderModel(BaseModel):
    owner = models.ForeignKey(CustomerModel, related_name="related_customer_cart",on_delete=models.PROTECT)
    cost = models.FloatField(default=0)
    tax = models.FloatField(default=0.05)
    total_amt = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    cancellation_request = models.BooleanField(default=False)
    coupon_applied = models.BooleanField(default=False)
    razorpay_order_id = models.CharField(max_length=50, null=True, blank=True, editable=False)
    razorpay_payment_id = models.CharField(max_length=50, null=True, blank=True, editable=False)
    razorpay_signature = models.CharField(max_length=50, null=True, blank=True, editable=False)
    invoice = models.FileField(upload_to="invoice", max_length=100, null=True, blank=True)


class OrderItemsModel(BaseModel):
    owner = models.ForeignKey(CustomerModel, on_delete=models.CASCADE, related_name="related_customer_cart_items")
    cart = models.ForeignKey(OrderModel, related_name="related_cart", on_delete=models.CASCADE)
    item = models.ForeignKey(ProductModel, related_name="related_items", on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    total = models.FloatField(default=0)


class CouponsModel(BaseModel):
    coupon_name = models.CharField(max_length=100, unique=True)
    coupon_discount_amount = models.FloatField(default=0.2)
    use_times = models.PositiveIntegerField(default=10)
    def __str__(self):
        return self.coupon_name


@receiver(pre_save, sender=OrderItemsModel)
def get_items_total(sender, instance, *args, **kwargs):
    instance.total = instance.item.price * instance.quantity


@receiver(post_save, sender=OrderItemsModel)
def get_total_amt(sender, instance, *args, **kwargs):
    total = 0
    cart_obj = OrderModel.objects.get(owner = instance.owner, is_paid=False)
    total = float(OrderItemsModel.objects.filter(cart=cart_obj).aggregate(Sum("total")).get("total__sum"))
    cart_obj.cost = total
    total += (cart_obj.tax*total)
    cart_obj.total_amt = total
    cart_obj.save()


@receiver(pre_save, sender=CouponsModel)
def coupon_update(sender, instance, *args, **kwargs):
    instance.use_times -= 1
    if instance.use_times < 1:
        instance.delete()
