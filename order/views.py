from django.shortcuts import render
from order.serializer import CartSerializer, CartItemSetializer, SimplifyAddCartItemSerializer
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from order.models import Cart, CartItem

class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet): 

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SimplifyAddCartItemSerializer
        else:
            return CartItemSetializer  

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}  
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
    
