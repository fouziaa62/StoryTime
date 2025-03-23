from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Story, Profile


class StoryTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.story = Story.objects.create(
            title='Test Story',
            content='This is a test story content.',
            author=self.user
        )

    def test_story_list_view(self):
        response = self.client.get(reverse('story_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Story')

    def test_story_detail_view(self):
        response = self.client.get(
            reverse('story_detail', args=[self.story.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test story content.')

    def test_add_story_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_story'), {
            'title': 'Another Test Story',
            'content': 'This is another test story content.'
        })
        self.assertEqual(response.status_code, 302)
        # Redirect after successful post
        self.assertTrue(
            Story.objects.filter(title='Another Test Story').exists()
        )

    def test_delete_story_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('delete_story', args=[self.story.id])
        )
        self.assertEqual(response.status_code, 302)
        # Redirect after successful delete
        self.assertFalse(Story.objects.filter(id=self.story.id).exists())


class ProfileTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.profile = Profile.objects.create(
            user=self.user, bio='This is a test bio.'
        )

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This is a test bio.')

    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_profile'), {
            'bio': 'Updated bio.'
        })
        self.assertEqual(response.status_code, 302)
        # Redirect after successful post
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio.')

    def test_delete_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(
            reverse('delete_profile')
        )
        self.assertEqual(response.status_code, 302)
        # Redirect after successful delete
        self.assertFalse(User.objects.filter(username='testuser').exists())
