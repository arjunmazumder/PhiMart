from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category, Review

class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField(read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']

    


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()

    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     view_name='view-specific-category'
    # )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category', 'price_with_tax']

    def get_price_with_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    def validate_price(self, price):

        if price < 0:
            raise serializers.ValidationError('Price could not be negative')
        return price


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        reviwe = Review.objects.create(product_id=product_id, **validated_data)
        return reviwe  