"""
from django.urls import path, include
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('', PostListView.as_view(), name='home'),
]
"""
