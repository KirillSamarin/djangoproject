from django.db import models
from users.models import CustomUser

class Category(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, verbose_name="наименование")
    description = models.TextField(null=True, blank=True, verbose_name="описание")

    def __str__(self):
        return f"{self.name}, {self.description}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

class Product(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255, verbose_name="наименование")
    description = models.TextField(null=True, blank=True, verbose_name="описание")
    image = models.ImageField(upload_to="photos/", verbose_name="изображение", null=True, blank=True)
    category = models.ForeignKey(Category, verbose_name="категория", on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField(verbose_name="цена за покупку")
    owner = models.ForeignKey(CustomUser, verbose_name='владелец', on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="дата последнего изменения")

    def __str__(self):
        return f"{self.name}, {self.category}, {self.description}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        permissions = [("can_unpublish_product", "может отменять публикацию продукта")]