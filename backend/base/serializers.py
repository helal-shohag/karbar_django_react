from rest_framework import serializers
from .models import  Category, Product, Order,Review    


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


