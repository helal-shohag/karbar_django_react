from django.shortcuts import render
from  .serializers import CategorySerializer, ProductSerializer, OrderSerializer,reviewSerializers,UserSerializer,UserSerializerWithToken
from django.contrib.auth.models import User
from .models import Category, Product
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k,v in serializer.items():
            data[k] = v
        
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
        first_name = data['name'],
        username = data['name'],
        email = data['email'],
        password = make_password(data['password'])
    ) 
    serializer = UserSerializerWithToken(user,many =False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([])
def userProfile(request):
    user = request.user
    serilizer = UserSerializer(user,many = False)
    return Response(serilizer.data)

@api_view(['GET'])
def getUsers(request):
    users =User.objects.all()
    serializers = UserSerializer(users,many=True  )
    return Response(serializers.data)



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