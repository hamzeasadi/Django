from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse


class SimpleTest(SimpleTestCase):

    def home_page_test(self):
        resp = self.client.get('/')
        print(resp.status_code)
        self.assertEqual(resp.status_code, 200)

    def about_page_test(self):
        resp = self.client.get(reverse('about'))
        print(reverse('about'))
        self.assertEqual(resp.status_code, 200)
