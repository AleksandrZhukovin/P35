from django import forms
from .models import User, Product, Director, Film
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# class WaterForm(forms.Form):
#     name = forms.CharField()
#     month = forms.IntegerField()
#     volume = forms.ChoiceField(choices=[['5', '5'], ['10', '10']])


class DirectorAdd(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'surname']


class FilmAdd(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'create_date', 'plot', 'director']


class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
        widgets = {'email': forms.EmailInput(attrs={'id': 'email', 'placeholder': 'Email', 'class': 'reg_field'}),
                   'username': forms.TextInput(attrs={})}


class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ComplainForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'id': 'name_id', 'class': 'style1'}))
    surname = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput())
    phone = forms.CharField()
    title = forms.CharField()
    date = forms.DateField(widget=forms.DateInput(attrs={'id': 'test_id', 'required': False}))  # mm-dd-yyyy


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']
