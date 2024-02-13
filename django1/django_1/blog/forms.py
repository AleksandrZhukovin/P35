from django.contrib.auth.forms import UserCreationForm
from django_1_app.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
