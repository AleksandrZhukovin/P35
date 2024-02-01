from django import forms
from .models import User, Product, Director, Film, Phones, News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ['name', 'email', 'surname', 'phone', 'comment']
        widgets = {'name': forms.TextInput(attrs={'class': 'form_field', 'placeholder': 'Name'}),
                   'email': forms.EmailInput(attrs={'class': 'form_field', 'placeholder': 'Email'}),
                   'surname': forms.TextInput(attrs={'class': 'form_field'}),
                   'phone': forms.TextInput(attrs={'class': 'form_field'}),
                   'comment': forms.TextInput(attrs={'class': 'form_field'})}


class PhonesFormEdit(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ['name', 'email', 'surname', 'phone', 'comment']
        widgets = {'name': forms.TextInput(attrs={'required': False}),
                   'email': forms.EmailInput(attrs={'required': False}),
                   'surname': forms.TextInput(attrs={'required': False}),
                   'phone': forms.TextInput(attrs={'required': False}),
                   'comment': forms.TextInput(attrs={'required': False})}



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


class NewsAdd(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text']

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
