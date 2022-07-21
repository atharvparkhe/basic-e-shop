from django.contrib import admin
from .models import *


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['owner', 'is_paid', 'cost', 'tax', 'total_amt']
admin.site.register(OrderModel,OrderModelAdmin)


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['item','quantity','total']
admin.site.register(OrderItemsModel, OrderItemsAdmin)


class CouponsAdmin(admin.ModelAdmin):
    list_display = ["coupon_name", "use_times", "coupon_discount_amount"]
admin.site.register(CouponsModel, CouponsAdmin)
