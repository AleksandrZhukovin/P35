from django.test import TestCase
from django_1.models import Post, User


class ModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        name = ['Bob', 'Jack', 'Ann', 'Kate', 'Johnny', 'Jim', 'Tom', 'Walter', 'Joe']
        for i in range(10):
            User.objects.create_user(username=name[i], email=f'{name[i]}@gmail.com', password='12345')
        for i in range(4):
            p = Post(text='test', user=User.objects.get(id=i + 1))
            p.save()

    def setUp(self):
        p = Post(text='test', user=User.objects.get(id=3))
        p.save()

    def test_1(self):
        post = Post.objects.get(id=2)
        self.assertEqual(post._meta.get_field('text').max_length, 200)

    def test_2(self):
        post = Post.objects.get(id=2)
        self.assertEqual('21', post.created_at.strftime('%H'))

    def test_3(self):
        post = Post.objects.get(id=3)
        self.assertEqual('Ann', post.user.username)
