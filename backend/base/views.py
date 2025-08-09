from django.shortcuts import render

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
    products = [
  {
    'id': 1,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    'description':'This is Product Brand Name Karbar since 21025',
    'rating':3,
    'review':10,
    'image':'/images/airpods.jpg',
    'discount': 30,
    'old_price': 200,  
    'stock':20
  },
  {
    'id': 2,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 3,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 60.0,
    'old_price': 100.5,
  },
  {
    'id': 4,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 100.0,
    'old_price': 150.0,
  },
  {
    'id': 5,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 6,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 7,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 8,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 9,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 10,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 11,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 12,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 13,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 14,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 15,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 16,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 17,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 18,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 19,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 20,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 21,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 22,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 23,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 24,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 25,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 26,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 27,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 28,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 29,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 30,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 31,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 32,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 33,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 34,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 35,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 36,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",

    'new_price': 85.0,
    'old_price': 120.5,
  },
]
    return Response(products)

@api_view(['GET'])
def Products_id(request,pk):
    products = [
  {
    'id': 1,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    'description':'This is Product Brand Name Karbar since 21025',
    'rating':3,
    'review':10,
    'image':'/images/airpods.jpg',
    'discount': 30,
    'old_price': 200,  
    'stock':20
  },
  {
    'id': 2,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 3,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 60.0,
    'old_price': 100.5,
  },
  {
    'id': 4,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 100.0,
    'old_price': 150.0,
  },
  {
    'id': 5,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 6,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 7,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 8,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 9,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 10,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 11,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 12,
    'name': "Striped Flutter Sleeve Overlap Collar Peplum Hem Blouse",
    'category': "women",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 13,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 14,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 15,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 16,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 17,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 18,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 19,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 20,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 21,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 22,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",

    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 23,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 24,
    'name': "Men Green Sol'id' Zippered Full-Zip Slim Fit Bomber Jacket",
    'category': "men",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 25,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 26,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 27,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 28,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 29,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
    
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 30,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 31,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 32,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 33,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
   
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 34,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
  
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 35,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",
 
    'new_price': 85.0,
    'old_price': 120.5,
  },
  {
    'id': 36,
    'name': "Boys Orange Colourblocked Hooded Sweatshirt",
    'category': "k'id'",

    'new_price': 85.0,
    'old_price': 120.5,
  },
]
    product = None
    for i in products:
        if i['id'] == pk:
            product = i
            break
    return Response(product)
