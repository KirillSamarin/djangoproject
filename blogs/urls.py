from django.urls import path
from .views import ArticleView, ArticleListView, ArticleUpdateView

app_name = 'blogs'

urlpatterns = [
    path('article/<int:pk>/', ArticleView.as_view(), name='article-detail'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-edit')
]