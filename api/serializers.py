from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов."""

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Цена должна быть больше 0")
        return value
