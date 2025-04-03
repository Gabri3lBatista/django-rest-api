from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):  # Usando ModelSerializer para criar um formulário baseado no modelo Product
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale_price',
            'get_discount',
        ] # Define os campos que serão exibidos no formulário