from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

@api_view()
def view_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(
        products,
        many = True,
        context = {'request': request}
    )

    return Response(serializer.data)

@api_view()
def view_specific_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product, context={'request': request})
    return Response(serializer.data)
 
@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serializer = CategorySerializer(category, context={'request': request}) 
    return Response(serializer.data)

@api_view()
def view_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True, context={'request': request})
    return Response(serializer.data)