from django.urls import path
from .views import getRoutes, Products_id,Products


urlpatterns = [
    path('',getRoutes,name='routes'),
    path('products/',Products,name='products'),
    path('products/<int:pk>/',Products_id,name='product'),
]
