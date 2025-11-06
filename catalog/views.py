from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView

class Home(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class Contacts(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'