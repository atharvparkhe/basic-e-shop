from rest_framework import serializers
from .models import *


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id", "name", "icon"]

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        exclude = ["id", "created_at", "updated_at"]


class AllProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["id", "name", "price", "img"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    recommendation = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        exclude = ["created_at", "updated_at"]
    def get_recommendation(self, obj):
        rec = []
        try:
            cart_obj = ProductModel.objects.get(id = obj.id)
            serializer = AllProductsSerializer(ProductModel.objects.filter(category=cart_obj.category).exclude(id=cart_obj.id), many=True)
            rec = serializer.data
            return rec
        except Exception as e:
            print(e)
