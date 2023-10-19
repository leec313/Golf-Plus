"""
context_processors.py was created to facilitate the like status of each blog
post. There was an issue when liking a post, moving to another page and
coming back to the liked post - the icon was not showing as liked.
This addresses the problem.
"""
from blog.models import Post


def liked_status(request):
    """
    Used to to include the liked status for the current user in every context
    """
    liked = False
    if request.user.is_authenticated:
        liked = Post.objects.filter(slug=request.resolver_match.kwargs.get(
            'slug'), likes=request.user).exists()
    return {'liked': liked}
