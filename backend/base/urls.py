from django.urls import path
from .views import  Products_id,Products,Categories,Categories_id,MyTokenObtainPairView,userProfile,getUsers,register

urlpatterns = [
    path('products/',Products,name='products'),
    path('products/<int:pk>/',Products_id,name='products'),
    path('categories/',Categories,name='categories'),
    path('categories/<int:pk>/',Categories_id,name='categories'),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/',userProfile,name='profile'),
    path('users/',getUsers,name='users'),
    path('register/',register,name='register'),
]
