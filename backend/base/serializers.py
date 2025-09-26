from rest_framework import serializers
from .models import  Category, Product, Order,Review    
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name =serializers.SerializerMethodField(read_only =True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','name','isAdmin']

    def get_name(self,obj):
        name = obj.first_name
        if name == '':
            name =obj.email

        return name     
    
    def get_isAdmin(self,obj):
        return obj.is_staff
    
class UserSerializerToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','name','isAdmin','token']

    def get_token(self,obj):
        token =RefreshToken.for_user(obj)
        return str(token)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
class reviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'review', 'rating']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


