from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('apply-coupon/', views.apply_coupon, name="apply-coupon"),
	path('buy-now/', views.buy_now, name="buy-now"),
	path('checkout/', views.checkout, name="checkout"),
	path('result/', views.resultPage, name="result"),
]