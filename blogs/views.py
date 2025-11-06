from django.urls import reverse_lazy

from blogs.models import Article
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blogs/article_form.html'
    fields = ['title', 'content', 'thumbnail', 'is_published']
    success_url = reverse_lazy('blogs:articles')

class ArticleView(DetailView):
    model = Article
    template_name = 'blogs/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.get_object()
        article.count_watches += 1
        article.save()
        return context

class ArticleListView(ListView):
    model = Article
    template_name = 'blogs/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(is_published=True).order_by('created_at')


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blogs/article_edit.html'
    fields = ['title', 'content', 'thumbnail', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blogs:article-detail', kwargs={"pk": self.object.pk})

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blogs/article_confirm_delete.html'
    success_url = reverse_lazy('blogs:articles')
