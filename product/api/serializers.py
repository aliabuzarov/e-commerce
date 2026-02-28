from rest_framework import serializers
from product.models import Product
from core.models import Subscribe

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source = 'category.name')

    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            'stock',
            'category',

        ]

class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = [
            'email'
        ]

class ProductCreateSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            'stock',
            'category',

        ]