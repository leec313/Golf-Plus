# URLS.PY for all blog related views
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostLike,
    CommentUpdateView,
    CommentDeleteView,
    subscribe_newsletter,
    ProfileView,
    delete_account,
    about,
    ContactView
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('subscribe_newsletter/', subscribe_newsletter,
         name='subscribe_newsletter'),
    path('profile/', ProfileView, name='profile'),
    path("about/", about, name='about'),
    path("contact/", ContactView, name='contact'),
    path('delete_account/', delete_account, name='delete_account'),
    path('like/<slug:slug>', PostLike.as_view(), name='post_like'),
    path('update/<slug:slug>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>/', PostDeleteView.as_view(), name='post_delete'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(),
         name='update_comment'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(),
         name='delete_comment'),
    path('', PostListView.as_view(), name='home'),
]
