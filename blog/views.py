from django.shortcuts import get_object_or_404, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    """
    View for listing all blog posts on the index.html
    Using the ListView method
    """
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetailView(DetailView):
    """
    View for showing a single post's details
    """
    model = Post
    template_name = "post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating a post and assigning a slug to the new post
    """
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content', 'featured_image', 'excerpt']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)

        # Add a message to inform the user
        messages.success(self.request, "Your post will display as soon as it is approved.")

        return response

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for creating a post and assigning a slug to the new post
    """
    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content', 'featured_image', 'excerpt']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        response = super().form_valid(form)

        # Add a message to inform the user
        messages.success(self.request, "Your post has been updated!.")

        return response

    # Checks to see if the user who created the post is the one updating it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for showing a single post's details
    """
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = '/'

    # Checks to see if the user who created the post is the one deleting it
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    # Add a message to inform the user
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your post has been deleted.")
        return super().delete(request, *args, **kwargs)



class PostLike(View):
    """
    View for liking a post
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
