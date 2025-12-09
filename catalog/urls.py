from django.urls import path
from .views import Home, Contacts, ProductDetail, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductUnpublishView, ListProductsCategory
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('product/<int:pk>/', cache_page(60)(ProductDetail.as_view()), name='product'),
    path('product/create', ProductCreateView.as_view(), name='new-product'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:pk>/unpublish', ProductUnpublishView.as_view(), name='product-unpublish'),
    path('category/<str:category_name>/', ListProductsCategory.as_view(), name='products_by_category')
]