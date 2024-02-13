from django.test import TestCase
from blog.form import RegistrationForm


class FormClass(TestCase):
    def test_1(self):
        form = RegistrationForm({'username': 'Test', 'password1': '12345', 'password2': '12345', 'email': 'name'})
        self.assertFalse(form.is_valid())

    def test_2(self):
        form = RegistrationForm({'username': 'Test', 'password1': '123', 'password2': '12345', 'email': 'name'})
        self.assertFalse(form.is_valid())

    def test_3(self):
        form = RegistrationForm({'username': 'Test', 'password1': 'super_password', 'password2': 'super_password',
                                 'email': 'name@gmail.com'})
        self.assertTrue(form.is_valid())

