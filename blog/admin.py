from django.contrib import admin
from .models import (
    Post,
    Comment,
    NewsletterSubscription,
    Profile,
    ContactModel
)
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin class for Post model
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    actions = ['approve_posts']
    
    # For bulk approval of posts
    def approve_posts(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for Comment model
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    # For bulk approval of comments
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(NewsletterSubscription)
class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin class for newsletter model
    """
    list_display = ('email', 'created_on')
    search_fields = ('email',)


# Register the profile model in the admin
admin.site.register(Profile)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin class for Contact model
    """
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
