from django.urls import path
from . import views
from .views import *

urlpatterns = [
	path('contact-us/', views.ContactUsView.as_view(), name="contact-us"),
	path('categories/', views.CategoryView.as_view(), name="all-categories"),
	path('all-products/', views.ProductView.as_view(), name="all-products"),
	path('products-by-category/<category_id>/', views.productByCategory, name="products-by-category"),
	path('product/<id>/', views.ProductRetriveView.as_view(), name="single-product"),
]