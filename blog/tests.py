from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostListTests(TestCase):
    def setUp(self):
        Post.objects.create(author='author1', content='testcontent',
                            title='testtitle1')

        Post.objects.create(author='author1', content='testcontent',
                            title='testtitle2')

        Post.objects.create(author='author2', content='testcontent',
                            title='testtitle3')

    def test_get_all_posts(self):
        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'بلاگ من')
        self.assertEqual(response.context['posts'].count(), Post.objects.count())

    def test_get_author_posts_success(self):
        response = self.client.get(reverse('author_posts', args=('author1',)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'بلاگ من')
        self.assertEqual(response.context['posts'].count(), Post.objects.filter(author='author1').count())

    def test_get_nonexisting_author_posts(self):
        response = self.client.get(reverse('author_posts', args=('author3',)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'بلاگ من')
        self.assertEqual(response.context['posts'].count(), 0)

