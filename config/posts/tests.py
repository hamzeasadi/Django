from django.test import TestCase
from django.urls import reverse
# from django.shortcuts import reverse, redirect
from .models import Post


class PostListViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text="I am totally doing greate")

    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        # print(resp)
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        url_name = self.client.get(reverse('home'))
        print(reverse('home'))
        self.assertEqual(url_name.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        # print(resp)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')
        # print(self.assertTemplateUsed(resp, 'home.html'))
