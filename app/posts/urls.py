from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('adicionar/', views.PostCreateView.as_view(), name='post-create'),
    path('atualizar/<int:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('apagar/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('detalhe/<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]

urlpatterns += [
    path('categorias/', views.CategoryList.as_view(), name='category-list'),
    path('categorias/adicionar/', views.CategoryCreateView.as_view(), name='category-create'),
    path('categorias/atualizar/<int:pk>', views.CategoryUpdateView.as_view(), name='category-update'),
    path('categorias/apagar/<int:pk>', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('categorias/<slug:slug>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('categorias/detalhe/<slug:slug>/', views.CategoryDetail.as_view(), name='category-detail'),
]
