
from rest_framework import serializers

from product.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    def get_products_count(self, category):
        return category.products.count()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars', 'product')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'reviews', 'description', 'price', 'category')
