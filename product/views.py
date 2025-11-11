from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category

@api_view()
def view_specific_product(request, id):
    product = Product.objects.get(pk=id)
    product_dic = {
        'id' : product.id,
        'name' : product.name,
        'price' : product.price
    }
    return Response(product_dic)
    
