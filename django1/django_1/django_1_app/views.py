from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    if request.method == 'POST':
        data = request.POST
        print(data['text'])
        name = 'Bob'
        return redirect('/page2')
    elif request.method == 'GET':
        name = 'Bob'
        # context = {'var': name}
        return render(request, 'home.html', {'var': name, 'l': [1, 2, 3, 4]})


def page2(request):
    return HttpResponse('Hello')