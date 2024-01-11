from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    name = 'Bob'
    # context = {'var': name}
    return render(request, 'home.html', {'var': name})
