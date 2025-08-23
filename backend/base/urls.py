from django.urls import path
from .views import getRoutes, Products_id,Products,Categories,Categories_id


urlpatterns = [
    path('',getRoutes,name='routes'),
    path('products/',Products,name='products'),
    path('products/<int:pk>/',Products_id,name='products'),
    path('categories/',Categories,name='categories'),
    path('categories/<int:pk>/',Categories_id,name='categories'),
]
