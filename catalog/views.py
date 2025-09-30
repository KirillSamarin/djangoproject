from django.shortcuts import render
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')

def product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, 'catalog/product.html', context)