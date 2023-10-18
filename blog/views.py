from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm


'''
View for listing all blog posts on the index.html
Using the ListView method
'''
class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

"""

"""
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"



class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
