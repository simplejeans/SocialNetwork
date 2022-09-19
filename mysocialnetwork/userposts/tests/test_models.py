from django.test import TestCase
from userposts.models import Post


class PostTestCase(TestCase):

    def post_creating(self):
        result = Post.objects.create(post_text='qwerty', pub_date='2022-09-19T08:36:34Z')
        self.assertEqual(Post.get(post_text='qwerty', pub_date='2022-09-19T08:36:34Z'), result)

