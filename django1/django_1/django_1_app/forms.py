from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class WaterForm(forms.Form):
    name = forms.CharField()
    month = forms.IntegerField()
    volume = forms.ChoiceField(choices=[['5', '5'], ['10', '10']])


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {'email': forms.EmailInput(attrs={'id': 'email'})}


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class ComplainForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name_id', 'class': 'style1'}))
    surname = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput())
    phone = forms.CharField()
    title = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'test_id', 'required': False}))  # mm-dd-yyyy
