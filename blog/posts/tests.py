from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import models as M
from django.utils import dates, timezone

# print(timezone.now().date())



class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@gmail.com',
            password='secret'
        )
        self.post = M.Post.objects.create(
            title='C++',
            content="""C++ is a general-purpose programming language""",
            author=self.user,
            date_posted=f'{timezone.now().date()}'
        )

    def test_string_representation(self):
        post = M.Post(title='a title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'C++')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.content}', "C++ is a general-purpose programming language")

    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "C++ is a general-purpose programming language")
        self.assertTemplateUsed(resp, 'index.html')

    def test_post_detail_view(self):
        resp = self.client.get('/post/1/')
        no_resp = self.client.get('/post/10/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(no_resp.status_code, 404)
        self.assertContains(resp, 'C++')
        self.assertTemplateUsed(resp, 'post_detail.html')



