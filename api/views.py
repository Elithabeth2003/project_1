from rest_framework import viewsets

from products.models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для продуктов."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
