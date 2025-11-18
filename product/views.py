from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly
# Model view set

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    permission_classes = [IsAdminOrReadOnly]
    # permission_classes = [IsAdminUser]
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     else:
    #         return [IsAdminUser()]


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewModelViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

 
# Function base views

# @api_view(['GET', 'POST'])
# def view_products(request):
#     if request.method == 'GET':
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(
#             products,
#             many = True,
#             context = {'request': request}
#         )
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# @api_view(['GET', 'PUT', 'DELETE'])
# def view_specific_product(request, pk):
#     if request.method == 'GET':
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     if request.method == 'DELETE':
#         product = get_object_or_404(Product, pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET','POST'])
# def view_categories(request):
#     if request.method == 'GET':
#         categories = Category.objects.annotate(product_count=Count('products')).all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = CategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 
# @api_view(['GET', 'PUT', 'DELETE'])
# def view_specific_category(request, pk):
#     if request.method == 'GET':
#         category = get_object_or_404(Category,pk=pk)
#         serializer = CategorySerializer(category) 
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         category = get_object_or_404(Category, pk=pk)
#         serializer = CategorySerializer(category, data=request.data, context = {'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#     if request.method == 'DELETE':
#         category = get_object_or_404(Category, pk=pk)
#         delete_data = category
#         category.delete()
#         serializer = CategorySerializer(delete_data, context = {'request': request})
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


#class base views

# class ViewProducts(APIView):
#     def get(self, request):
#         products = Product.objects.select_related('category').all()
#         serializer = ProductSerializer(
#             products,
#             many = True,
#             context = {'request': request}
#         )
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# class ViewSpecificProduct(APIView):
#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, context={'request': request})
#         return Response(serializer.data)
#     def put(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         serializer = ProductSerializer(product, data=request.data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

#     def delete(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         copy_data = product
#         product.delete()
#         serializer = ProductSerializer(copy_data, context = {'request': request})
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


# class ViewCategories(APIView):
#     def get(self, request):
#         categories = Category.objects.annotate(product_count=Count('products')).all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#     def post(self, request):
#         serializer = CategorySerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ViewSpecificCategory(APIView):
#     def get(self, request, pk):
#         category = get_object_or_404(
#             Category.objects.annotate(product_count=Count('products')).all(),
#             pk=pk
#         )
#         serializer = CategorySerializer(category) 
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         category = get_object_or_404(
#             Category.objects.annotate(product_count=Count('products')).all(), 
#             pk=pk
#         )
#         serializer = CategorySerializer(category, data=request.data, context = {'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def delete(self, request, pk):
#         category = get_object_or_404(
#             Category.objects.annotate(product_count=Count('products')).all(), 
#             pk=pk
#         )
#         delete_data = category
#         category.delete()
#         serializer = CategorySerializer(delete_data, context = {'request': request})
#         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


# Generic view class
# class ViewProducts(ListCreateAPIView):
#     def get_queryset(self):
#         return Product.objects.select_related('category').all()
#     def get_serializer_class(self):
#         return ProductSerializer
#     def get_serializer_context(self):
#         return {'request': self.request}


# class ViewSpecificProduct(RetrieveUpdateDestroyAPIView):
#     def get_queryset(self):
#         return Product.objects.select_related('category').all()
#     def get_serializer_class(self):
#         return ProductSerializer
#     def get_serializer_context(self):
#         return {'request': self.request}



# class ViewCategories(ListCreateAPIView):
#     def get_queryset(self):
#         return Category.objects.annotate(product_count=Count('products')).all()
#     def get_serializer_class(self):
#         return CategorySerializer
    
    
# class ViewSpecificCategory(RetrieveUpdateDestroyAPIView):
#     def get_queryset(self):
#         return Category.objects.annotate(product_count=Count('products')).all()
#     def get_serializer_class(self):
#         return CategorySerializer

