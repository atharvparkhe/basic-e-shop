from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.paginator import Paginator
from base.utils import paginate
from .serializers import *
from .models import *


class ContactUsView(ListCreateAPIView):
    queryset = ContactUsModel
    serializer_class = ContactUsSerializer
    # def list(self, request):
    #     try:
    #         authentication_classes = [JWTAuthentication]
    #         permission_classes = [IsAdminUser]
    #         serializer = self.serializer_class(self.queryset, many=True)
    #         return Response({"data":serializer.data}, status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CategoryView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
class CategoryCreate(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
class CategoryRetriveUpdate(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = "id"


class ProductView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = AllProductsSerializer


class ProductRetriveView(RetrieveAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"


@api_view(["GET"])
def productByCategory(request, category_id):
    try:
        if not CategoryModel.objects.filter(id=category_id):
            return Response({"message":"Invalid Category ID"}, status=status.HTTP_404_NOT_FOUND)
        category_obj = CategoryModel.objects.get(id=category_id)
        product_objs = ProductModel.objects.filter(category=category_obj)
        print(product_objs)
        ser = AllProductsSerializer(product_objs, many=True)
        return Response({"data":ser.data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
