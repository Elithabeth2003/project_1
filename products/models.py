from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    """Модель продукта."""

    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(
        max_length=256,
        verbose_name='Описание',
        unique=True)
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name[:50]
