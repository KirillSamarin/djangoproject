from django.db import models

class Article(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=255, verbose_name='заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='содержимое')
    thumbnail = models.ImageField(upload_to='photos/', verbose_name='превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания")
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    count_watches = models.IntegerField(verbose_name='количество просмотров')

    def __str__(self):
        return f"{self.title}, {self.content}"

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"