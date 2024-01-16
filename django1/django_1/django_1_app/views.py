from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, User
from pathlib import Path
from django.core.files import File


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


def page2(request):
    return HttpResponse('Hello')
