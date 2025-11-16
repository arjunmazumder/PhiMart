from django.shortcuts import render
from order.serializer import CartSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from order.models import Cart

class CartViewSet(CreateModelMixin, GenericViewSet, RetrieveModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
