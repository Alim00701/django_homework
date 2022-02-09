from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts_all, name='post_list'),
]
