from rest_framework import serializers
from .models import *


class loginSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)
    password = serializers.CharField(required = True)


class signupSerializer(serializers.Serializer):
    f_name = serializers.CharField(required = True)
    l_name = serializers.CharField(required = True)
    email = serializers.EmailField(required = True)
    phone = serializers.CharField(required = False)
    password = serializers.CharField(required = True)


class otpSerializer(serializers.Serializer):
    otp = serializers.IntegerField(required = True)
    pw = serializers.CharField(required = True)


class emailSerializer(serializers.Serializer):
    email = serializers.EmailField(required = True)


class CustomerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = ["f_name", "l_name", "email", "phone"]

# class RemoveAdminSerializer(serializers.Serializer):
#     text = serializers.CharField(required = True)
#     otp = serializers.IntegerField(required = True)

# class SellerDisplaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SellerModel
#         fields = ["f_name", "l_name", "email", "phone", "is_verified"]

# class SpecialEmailSerializer(serializers.Serializer):
#     sub = serializers.CharField(required = True)
#     body = serializers.CharField(required = True)
