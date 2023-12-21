from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-created_date'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — product.html
    template_name = 'separate_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'separate_news'


class PostSearch(ListView):
    model = Post
    ordering = '-created_date'
    template_name = 'search.html'
    context_object_name = 'news'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


# Представление для создания новости
class NewsCreate(CreateView):
    # Разработанная форма
    form_class = PostForm
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'news_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == '/news/articles/create/':
            post.type = 'AR'
        post.save()
        return super().form_valid(form)


# Представление для редактирования новости
class NewsUpdate(LoginRequiredMixin, UpdateView):
    # Разработанная форма
    form_class = PostForm
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'news_edit.html'


# Представление для удаления новости
class NewsDelete(DeleteView):
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news')


# Представление для создания статьи
class ArticlesCreate(CreateView):
    # Разработанная форма
    form_class = PostForm
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'articles_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'article'
        return super().form_valid(form)


# Представление для редактирования статьи
class ArticlesUpdate(LoginRequiredMixin, UpdateView):
    # Разработанная форма
    form_class = PostForm
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'articles_edit.html'


# Представление для удаления статьи
class ArticlesDelete(DeleteView):
    # Модель новости
    model = Post
    # Шаблон страницы
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('news')
