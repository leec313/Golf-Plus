from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "post_list.html"
    paginate_by = 6
