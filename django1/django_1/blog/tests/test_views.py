from django.test import TestCase
from django.urls import reverse


class ViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user()

    def test_1(self):
        resp = self.client.get('/')
        self.assertTrue(resp.status_code != 200)

    def test_2(self):
        resp = self.client.get('/')
        self.assertTrue('user' in resp.context.keys())

    def test_3(self):
        resp = self.client.get(reverse('posts'))
        self.assertTrue(res.status_code == 200)
