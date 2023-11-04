from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, NewsletterSubscription, Profile

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)
        self.comment = Comment.objects.create(body='Test Comment', post=self.post, user=self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post_new'), {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)  # 302 because it should redirect to the detail view
        self.assertTrue(Post.objects.filter(title='New Post').exists())
