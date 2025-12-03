from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm

class Home(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

class Contacts(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = 'catalog/home.html'

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'
    success_url = 'catalog/home.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = 'catalog/home.html'