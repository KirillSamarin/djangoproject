from django.urls import path
from .views import Home, Contacts, ProductDetail

app_name = 'catalog'

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product')
]