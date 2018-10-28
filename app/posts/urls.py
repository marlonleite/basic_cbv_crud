from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('adicionar/', views.PostCreateView.as_view(), name='post-create'),
    path('atualizar/<int:pk>', views.PostUpdateView.as_view(), name='post-update'),
    path('apagar/<int:pk>', views.PostDeleteView.as_view(), name='post-delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post-detail'),
]
