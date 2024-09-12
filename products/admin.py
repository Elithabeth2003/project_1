from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Админка для продуктов."""

    list_display = ('pk', 'name', 'description', 'price', 'image')
    search_fields = ('name',)
