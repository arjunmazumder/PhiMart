from django.shortcuts import render
from order.serializer import CartSerializer, CartItemSetializer, SimplifyAddCartItemSerializer, UpdateCartItemSerializer, OrderSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.models import Cart, CartItem, Order, OrderItem
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
# from order.services import OrderService
# from order import serializers as orderSz

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemViewSet(ModelViewSet): 
    http_method_names=['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SimplifyAddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        else:
            return CartItemSetializer  

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}  
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])


class OrderViewset(ModelViewSet):
    # queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)