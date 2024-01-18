from django.shortcuts import render, redirect
from .models import Product, User
from pathlib import Path
from django.core.files import File
from .forms import WaterForm, Registration, Login, ComplainForm
from django.contrib.auth import authenticate, login, logout


def home(request):
    user = User.objects.get(id=1)
    path = Path('static/images/R.jpg')
    with path.open(mode='rb') as img:
        file = File(img, name=img.name)
    product = Product(name='Apple', user=user, file=file)
    product.save()
    product = Product(name='banana', user=user, file=file)
    product.save()
    product = Product(name='orange', user=user, file=file)
    product.save()
    product = Product(name='tomato', user=user, file=file)
    product.save()
    # product.many_user.add(user)
    # product.save()
    # product.many_user.add(user)
    # product.save()
    # product.many_user.remove(user)
    # product.save()
    # print(product.many_user.all())
    if request.method == 'POST':
        data = request.POST
        print(data['text'])
        name = 'Bob'
        return redirect('/page2')
    elif request.method == 'GET':
        # data = Product.objects.all()  # QuerySet
        data = Product.objects.filter(id=1)   # QuerySet
        data[0].name = 'water'
        data[0].save()
        data[0].user.username # user object
        data[0].file  # file object
        return render(request, 'home.html', {'var': data, 'l': [1, 2, 3, 4]})


def main(request):
    return render(request, 'home.html', {'user': request.user})


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'])
            user.save()
            return redirect('/')
    else:
        return render(request, 'registration.html', {'form': Registration()})


def water(request):
    if request.method == 'POST':
        data = request.POST
        return render(request, 'water.html', data)
    else:
        form = ComplainForm()
        return render(request, 'water.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('/')
    else:
        return render(request, 'registration.html', {'form': Login()})


def logout_page(request):
    logout(request)
    return redirect('/')
