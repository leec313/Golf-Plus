from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Post, Comment, NewsletterSubscription


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
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')

        # Creating a test post associated with the test user and setting a slug
        self.post = Post.objects.create(
            title='Test Post', content='Test Content',
            author=self.user, slug='royal-portrush-golf-club')

        # Creating a test comment associated with the test post and user
        self.comment = Comment.objects.create(
            body='Test Comment', post=self.post, user=self.user)
        
        # URL for updating the post
        self.update_url = reverse(
            'post_update', kwargs={'slug': self.post.slug})

        # URL for deleting the post
        self.delete_url = reverse(
            'post_delete', kwargs={'slug': self.post.slug})

    def test_post_list_view(self):
        """Testing the post list view"""
        
        # Simulating a GET request to the 'post_list' URL
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_post_create_view(self):
        """Testing the post create view"""
        
        # Logging in with the test user
        self.client.login(username='testuser', password='testpassword')

        # Simulating a POST request to the 'post_new' URL with form data
        response = self.client.post(
            reverse('post_new'),
            {'title': 'New Post', 'content': 'New Content'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_post_detail_view(self):
        """Simulating GET request to the 'post_detail' URL for created post"""

        response = self.client.get(
            reverse('post_detail', args=[self.post.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_newsletter_subscription(self):
        """Simulate POST request to 'subscribe_newsletter' URL w/ form data"""

        response = self.client.post(
            reverse('subscribe_newsletter'), {'email': 'test@example.com'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(NewsletterSubscription.objects.filter(
            email='test@example.com').exists())

    def test_post_update_view(self):
        """Testing the post update view"""
        
        self.client.login(username='testuser', password='testpassword')

        # Simulating a GET request to the 'post_update' URL
        response = self.client.get(self.update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_form.html')

        # Simulating a POST request to the 'post_update' URL with form data
        updated_title = 'Updated Post Title'
        response = self.client.post(self.update_url, {
            'title': updated_title, 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 302)

        # Check if the post is updated in the database
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, updated_title)

    def test_post_delete_view(self):
        """Testing the post delete view"""
        
        self.client.login(username='testuser', password='testpassword')

        # Simulating a GET request to the 'post_delete' URL
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_confirm_delete.html')

        # Simulating a POST request to confirm the deletion
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the expected success URL
        expected_redirect_url = reverse('home')
        self.assertRedirects(response, expected_redirect_url)

        # Check if the post is deleted from the database
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())

        # Check if a success message is added
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your post has been deleted.")

    def test_post_comment(self):
        """Testing posting a comment on a post"""
        
        self.client.login(username='testuser', password='testpassword')

        # Simulating a POST request to the 'post_detail' URL with comment data
        response = self.client.post(
            reverse('post_detail', kwargs={
                'slug': self.post.slug}), {'body': 'Test Comment'})

        # Asserting that the response status code is 200 after posting comment
        self.assertEqual(response.status_code, 200)

        # Check if the comment is added to the database
        self.assertTrue(Comment.objects.filter(
            body='Test Comment', post=self.post, user=self.user).exists())

        # Check if the success message is added
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Comment posted!")

        # Check if the comment is displayed in the post detail page
        self.assertContains(response, 'Test Comment')

    def test_comment_update_view(self):
        """Testing the comment update view"""

        self.client.login(username='testuser', password='testpassword')

        # Simulating a GET request to the 'comment update' URL
        response = self.client.get(reverse(
            'update_comment', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment_update.html')

        # Simulate POST request to 'comment_update' URL w/updated comment data
        updated_body = 'Updated Test Comment'
        response = self.client.post(reverse(
            'update_comment', kwargs={
                'pk': self.comment.pk}), {'body': updated_body})
        self.assertEqual(response.status_code, 302)

        # Check if the comment is updated in the database
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.body, updated_body)

        # Check if the success message is added
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your comment has been updated.")

    def test_comment_delete_view(self):
        """Testing the comment delete view"""
        
        self.client.login(username='testuser', password='testpassword')

        # Simulating a GET request to the 'comment delete' URL
        response = self.client.get(reverse(
            'delete_comment', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment_delete.html')

        # Simulating a POST request to confirm the deletion
        response = self.client.post(reverse(
            'delete_comment', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, 302)

        # Check if the comment is deleted from the database
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

        # Check if the success message is added
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "Your comment has been deleted.")

    def test_post_like_view(self):
        """Testing the post like view"""

        self.client.login(username='testuser', password='testpassword')

        # Simulating a POST request to the 'post_like' URL
        response = self.client.post(reverse(
            'post_like', kwargs={'slug': self.post.slug}))
        self.assertEqual(response.status_code, 302)

        # Check if the user's like status for the post is toggled
        self.post.refresh_from_db()
        self.assertEqual(self.post.likes.filter(
            id=self.user.id).exists(), True)

        # Redirect to the same URL to avoid issues with refreshing
        self.assertRedirects(response, reverse(
            'post_detail', kwargs={'slug': self.post.slug}))

    def test_404_page(self):
        # Simulate a GET request to a non-existent URL
        response = self.client.get('non_existent_url')

        # Check if the response status code is 404
        self.assertEqual(response.status_code, 404)

        # Check if the 404 template is used
        self.assertTemplateUsed(response, '404.html')
