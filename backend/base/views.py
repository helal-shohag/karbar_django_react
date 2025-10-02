from django.shortcuts import render
from  .serializers import CategorySerializer, ProductSerializer, OrderSerializer,reviewSerializers,UserSerializer,UserSerializerToken
from .models import Category, Product
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from rest_framework import status
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

class tokenSerializer(TokenObtainPairSerializer):
    def validate(self,attrs):
        data =super().validate(attrs)

        serializer = UserSerializerToken(self.user).data
        for k,v in serializer.items():
            data[k]=v

        return data
    
class myTokenView(TokenObtainPairView):
    serializer_class = tokenSerializer

@api_view(['POST'])
def RegisterUser(request):
    data = request.data
    try:
        user = User.objects.create_user(
        first_name = data['name'],
        username = data['email'],
        email = data['email'],
        password = make_password(data['password'])
    ) 
        serializer = UserSerializerToken(user,many=False)

        return Response(serializer.data)
    except:
          message = {'detail':'User with this email already exists'}
          return Response(message,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def users_profile(request):
    user = request.user
    serilaizer = UserSerializer(user,many =True)
    return Response(serilaizer.data)

@api_view(['GET'])
def users(request):
    user = User.objects.all()
    serilaizer = UserSerializer(user, many=True)
    return Response(serilaizer.data)

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