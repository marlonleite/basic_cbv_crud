from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import (Post, Category)


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'slug', 'content', 'author', 'category']
    template_name_suffix = '_create'
    success_url = reverse_lazy('posts:post-list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'slug', 'content', 'author', 'category']
    template_name_suffix = '_update'
    success_url = reverse_lazy('posts:post-list')


class PostDeleteView(DeleteView):
    model = Post
    template_name_suffix = '_delete'
    success_url = reverse_lazy('posts:post-list')


class CategoryList(ListView):
    model = Category


class CategoryDetail(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['title', 'slug']
    template_name_suffix = '_create'
    success_url = reverse_lazy('posts:category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['title', 'slug']
    template_name_suffix = '_update'
    success_url = reverse_lazy('posts:category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name_suffix = '_delete'
    success_url = reverse_lazy('posts:category-list')
