from django.urls import path
from .views import Home, Contacts, ProductDetail, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductUnpublishView

app_name = 'catalog'

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='new-product'),
    path('product/<int:pk>/edit', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('product/<int:pk>/unpublish', ProductUnpublishView.as_view(), name='product-unpublish')
]