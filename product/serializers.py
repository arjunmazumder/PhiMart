from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='view-specific-product'
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'price_with_tax']

    def get_price_with_tax(self, product):
        return round(product.price * Decimal(1.1), 2)