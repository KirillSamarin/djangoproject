from .models import Product, Category
from django.shortcuts import get_object_or_404


def get_products_by_category(category_name):
    category = get_object_or_404(Category, name=category_name)
    return Product.objects.filter(category=category, is_published=True)