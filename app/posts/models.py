from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:category-detail', kwargs={'slug': self.slug})


class Post(models.Model):
    title = models.CharField('Título', max_length=100)
    slug = models.SlugField(unique=True)
    content = models.TextField('Conteúdo')
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    modified_at = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Notícia'
        verbose_name_plural = 'Notícias'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post-detail', kwargs={'slug': self.slug})
