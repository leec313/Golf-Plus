from django.shortcuts import get_object_or_404, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
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


class PostCreateView(CreateView):
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
