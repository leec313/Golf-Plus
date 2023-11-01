from .models import (
    Post,
    Comment,
    NewsletterSubscription,
    Profile,
    ContactModel
)
from django.contrib.auth.models import User
from django.forms import ImageField, FileInput
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt']


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Your comment here'}))

    class Meta:
        model = Comment
        fields = ('body',)


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter your email'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ImageUpdateForm(forms.ModelForm):
    image = ImageField(widget=FileInput)

    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = 'Profile Picture'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)