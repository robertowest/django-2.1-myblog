from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.base_index, name='base_index'),
    path('posts', views.list_posts, name='list_posts'),
    path('post/add', views.base_post_add, name='base_post_add'),
    path('post/<int:pk>/', views.base_post, name='base_post'),
    path('post/<int:pk>/comment/', views.base_comment, name='base_comment'),
    path('post/<int:pk>/edit/', views.base_post_edit, name='base_post_edit'),
]
