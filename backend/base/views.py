from django.shortcuts import render
from  .serializers import CategorySerializer, ProductSerializer, OrderSerializer,reviewSerializers
from .models import Category, Product
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/products/',
        'api/products/create/',
        'api/products/upload',
        'api/products/top/',
        'api/products/<id>/',
        'api/products/delete/<id>',
        'api/products/update/<id>',

    ]
    return Response(routes)

@api_view(['GET'])
def Products(request):
   products = Product.objects.all()
   serializers = ProductSerializer(products, many=True)
   return Response(serializers.data)

@api_view(['GET'])
def Products_id(request, pk):
    product = Product.objects.get(_id=pk)
    serializers = ProductSerializer(product, many=False)
    return Response(serializers.data)
@api_view(['GET'])
def Categories(request):
    categories = Category.objects.all()
    serializers = CategorySerializer(categories, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def Categories_id(request, pk):
    category = Category.objects.get(id=pk)
    serializers = CategorySerializer(category, many=False)
    return Response(serializers.data)