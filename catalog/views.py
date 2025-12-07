from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from .forms import ProductForm

class Home(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.user.has_perm('catalog.can_unpublish_product'):
            return Product.objects.all()
        return Product.objects.filter(is_published=True)

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

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_published = True
        self.object.save()
        return redirect(self.get_success_url())

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'
    success_url = 'catalog/home.html'

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = 'catalog/home.html'


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_unpublish.html'
    permission_required = 'catalog.can_unpublish_product'
    success_url = 'catalog/home.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_published = False
        self.object.save()
        return redirect(self.get_success_url())
