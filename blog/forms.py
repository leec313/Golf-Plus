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


class PostForm(forms.ModelForm):
    """
    Form class for creating a blog post
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'excerpt']


class CommentForm(forms.ModelForm):
    """
    Form class for posting a comment
    """
    body = forms.CharField(widget=forms.Textarea(
            attrs={'placeholder': 'Your comment here'}))

    class Meta:
        model = Comment
        fields = ('body',)


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Newsletter form class
    """
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter your email'})


class ProfileUpdateForm(forms.ModelForm):
    """
    Form class so users can update their profile info
    """
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        # Check if the email is already taken by another user
        if User.objects.filter(
                email=email).exclude(username=username).exists():
            raise forms.ValidationError(
                'This email address is already in use.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        # Check if the username is already taken by another user
        if User.objects.filter(
                username=username).exclude(email=email).exists():
            raise forms.ValidationError('This username is already in use.')
        return username


class ProfileNewsletterUpdate(forms.ModelForm):
    """
    Form class for updating the newsletter subscription on the profile
    """
    subscribe_newsletter = forms.BooleanField(
        label='Subscribe to Newsletter',
        required=False,
    )

    class Meta:
        model = NewsletterSubscription
        fields = ['subscribe_newsletter']


class ImageUpdateForm(forms.ModelForm):
    """
    Form class so users can update their profile picture
    """
    image = ImageField(widget=FileInput)

    class Meta:
        model = Profile
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(ImageUpdateForm, self).__init__(*args, **kwargs)
        self.fields['image'].label = 'Profile Picture'


class ContactForm(forms.ModelForm):
    """
    Contact page form class
    """
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
