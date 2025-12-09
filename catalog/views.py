from django.urls import reverse_lazy
from django.core.cache import cache
from .models import Product, Category
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from .forms import ProductForm
from .services import get_products_by_category

class ListProductsCategory(ListView):
    model = Product
    template_name = 'catalog/products_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        category_name = self.kwargs.get('category_name')

        if not category_name:
            return Product.objects.filter(is_published=True)

        if self.request.user.groups.filter(name='Managers').exists():
            category = get_object_or_404(Category, name=category_name)
            return Product.objects.filter(category=category)

        return get_products_by_category(category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.kwargs.get('category_name', 'Все продукты')
        context['category_name'] = category_name
        context['page_title'] = f'Категория: {category_name}'
        return context


class Home(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        user = self.request.user

        if user.groups.filter(name='Managers').exists():
            return Product.objects.all()

        cache_key = 'public_published_products'
        queryset = cache.get(cache_key)

        if queryset is None:
            queryset = Product.objects.filter(is_published=True)
            cache.set(cache_key, queryset, 60 * 15)

        return queryset

class Contacts(TemplateView):
    template_name = 'catalog/contacts.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product.html'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.is_published = True
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_edit.html'
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('catalog.change_product'):
            return HttpResponseForbidden("У вас нет прав для изменения этого продукта.")
        return super().post(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('catalog.delete_product'):
            return HttpResponseForbidden("У вас нет прав для удаления этого продукта.")
        return super().post(request, *args, **kwargs)

class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_unpublish.html'
    permission_required = 'catalog.can_unpublish_product'
    success_url = reverse_lazy('catalog:home')

    def post(self, request, *args, **kwargs):
        if not request.user.has_perm('catalog.can_unpublish_product'):
            return HttpResponseForbidden("У вас нет прав для отмены публикации продукта.")

        self.object = self.get_object()
        self.object.is_published = False
        self.object.save()
        return redirect(self.get_success_url())
