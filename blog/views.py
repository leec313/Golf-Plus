from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, NewsletterSubscription, Profile
from .forms import (
    CommentForm,
    NewsletterSubscriptionForm,
    ProfileUpdateForm,
    ImageUpdateForm
)
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


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

    def get_context_data(self, **kwargs):
        """
        Used for calling the newsletter modal form
        """
        context = super().get_context_data(**kwargs)
        context['form'] = NewsletterSubscriptionForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)

        if search_query:
            # Use Q objects to combine filters with OR logic
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(author__username__icontains=search_query) |
                Q(content__icontains=search_query) |
                Q(excerpt__icontains=search_query)
            )

        return queryset

    def render_to_response(self, context, **response_kwargs):
        # Check if no posts are found based on the search query
        if not context['posts']:
            context['no_results'] = True  # Add a flag to indicate no results

        return super().render_to_response(context, **response_kwargs)


class PostDetailView(DetailView):
    """
    View for showing a single post's details
    """
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Your existing logic for getting the post details
        post = context['post']
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Adding the comment form to the context
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        context['comments'] = comments

        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data()

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        # Retrieve the post using the same logic as in the get method
        self.object = self.get_object()
        context = self.get_context_data()

        # Retrieve the comment form from the request
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = self.object
            comment.save()
        else:
            comment_form = CommentForm()

        # Add the comment form to the context
        context['comment_form'] = comment_form
        context['commented'] = True

        return render(request, "post_detail.html", context)


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
        messages.success(self.request,
                         "Your post will display as soon as it is approved.")

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
    View for deleting a single post
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
    View for liking a post. If liked, the view passes the information
    to the template to show the updated icon for confirmation of like
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        # Toggle the like status for the user
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        # Redirect to the same URL to avoid issues with refreshing
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def subscribe_newsletter(request):
    """
    Used to post the email the user inputs to the database and
    displays a success/error message
    """
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for subscribing.")
            return redirect('home')
        else:
            messages.error(request,
                           "This email address is already subscribed.")
            return redirect('home')

    return render(request, 'subscribe_modal.html', {'form': form})


def ProfileView(request):
    user_form = ProfileUpdateForm(instance=request.user)
    image_form = ImageUpdateForm(instance=request.user.profile)
    user_posts = Post.objects.filter(author=request.user)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(user_posts, 6)  # Show 3 posts per page
    try:
        user_posts = paginator.page(page)
    except PageNotAnInteger:
        user_posts = paginator.page(1)
    except EmptyPage:
        user_posts = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        image_form = ImageUpdateForm(
             request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and image_form.is_valid():
            user_form.save()
            image_form.save()
            return redirect('profile')

    return render(request, 'profile.html',
                  {'user_form': user_form,
                   'image_form': image_form, 'user_posts': user_posts})


@login_required
def delete_account(request):
    if request.method == 'POST':
        # Delete the user and redirect to the home page
        request.user.delete()
        return redirect('home')

    return render(request, 'delete_account.html')