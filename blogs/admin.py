from django.contrib import admin
from .models import Article

@admin.register(Article)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("title", "content")
