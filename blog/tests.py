from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, NewsletterSubscription, Profile


# UNCOMMENT LINES 129-135 IN SETTINGS.PY AND COMMENT LINES 138-140 
# BEFORE RUNNING THE TESTS.PY


class BlogTests(TestCase):
    """
    Setting up the testing environment before each test method runs
    """
    def setUp(self):
        # Creating a test client to simulate HTTP requests
        self.client = Client()

        # Creating a test user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Creating a test post associated with the test user
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

        # Creating a test comment associated with the test post and user
        self.comment = Comment.objects.create(body='Test Comment', post=self.post, user=self.user)

    def test_post_list_view(self): # Testing the post list view
        
        # Simulating a GET request to the 'post_list' URL
        response = self.client.get(reverse('post_list'))

        # Asserting that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Asserting that the correct template is used for rendering the response
        self.assertTemplateUsed(response, 'index.html')

    def test_post_create_view(self): # Testing the post create view

        # Logging in with the test user
        self.client.login(username='testuser', password='testpassword')

        # Simulating a POST request to the 'post_new' URL with form data
        response = self.client.post(reverse('post_new'), {'title': 'New Post', 'content': 'New Content'})

        # Asserting that the response status code is 302 (redirect)
        # because it should redirect to the detail view after creating a new post
        self.assertEqual(response.status_code, 302)

        # Asserting that a post with the specified title now exists in the database
        self.assertTrue(Post.objects.filter(title='New Post').exists())
