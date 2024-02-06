from django.shortcuts import render, redirect
from .models import Product, User, Film, Director, Phones, News
from pathlib import Path
from django.core.files import File
from .forms import ProductForm, Registration, Login, FilmAdd, DirectorAdd, PhonesForm, PhonesFormEdit, NewsAdd
from django.contrib.auth import authenticate, login, logout
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from .models import News, Like
from django.http import JsonResponse


class LikeNews(TemplateView):
    def get(self, request, *args, **kwargs):
        news = News.objects.get(id=self.kwargs['id'])
        likes = Like.objects.filter(news=news)
        for i in likes:
            if i.user == self.request.user:
                i.delete()
                break
        else:
            l = Like(news=news, user=self.request.user)
            l.save()
        return redirect('/news')


def create_phone(request):
    if request.method == 'POST':
        form = PhonesForm(request.POST)
        if form.is_valid():
            phone = Phones(name=form.cleaned_data['name'], email=form.cleaned_data['email'],
                           surname=form.cleaned_data['surname'], phone=form.cleaned_data['phone'],
                           comment=form.cleaned_data['comment'])
            phone.save()
            return redirect('/')
    else:
        return render(request, 'phone_create.html', {'form': PhonesForm(), 'title': 'Phone Add'})


class PhoneCreate(CreateView):
    template_name = 'phone_create.html'
    # model = Phones
    form_class = PhonesForm
    # fields = ['name', 'email', 'surname', 'phone', 'comment']
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Phone Add'
        return context


def phones_page(request):
    phones = Phones.objects.all()
    return render(request, 'phones.html', {'phones': phones})


class PhonesPage(ListView):
    template_name = 'phones.html'
    model = Phones
    context_object_name = 'phones'


class NewsPage(TemplateView):
    template_name = 'phones.html'

    def get(self, request, *args, **kwargs):
        order = self.kwargs['sort']
        news = News.objects.all().order_by(order)
        return render(request, 'phones.html', {'news': news})


class OneNewsPage(TemplateView):
    template_name = 'phones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = News.objects.get(id=self.kwargs['id'])
        context['date'] = news.created_at.strftime('%Y-%m-%d')
        context['news'] = news
        return context


class NewsCreate(CreateView):
    template_name = ''
    form_class = NewsAdd
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class HomePage(ListView):
    template_name = 'home.html'
    model = Product
    context_object_name = 'products'


def phone_page(request, **kwargs):
    phone = Phones.objects.get(id=kwargs['id'])
    if request.method == 'POST':
        form = PhonesFormEdit(request.POST)
        if form.is_valid():
            phone.name = form.cleaned_data['name']
            phone.surname = form.cleaned_data['surname']
            phone.email = form.cleaned_data['email']
            phone.phone = form.cleaned_data['phone']
            phone.comment = form.cleaned_data['comment']
            phone.save()
            return redirect(f'/phone/{phone.id}')
    else:
        form = PhonesFormEdit(initial={'user': phone.name, 'surname': phone.surname,
                                       'phone': phone.phone, 'email': phone.email,
                                       'comment': phone.comment})
        return render(request, 'phone.html', {'phone': phone, 'form': form})


class PhonePage(UpdateView):
    template_name = 'phone.html'
    form_class = PhonesForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['phone'] = Phones.objects.get(id=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return f'/phone/{self.kwargs["pk"]}'


class Search(TemplateView):
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        pass

    def post(self, request):
        search_text = request.POST['text']
        res = Phones.objects.filter(name__contains=search_text)
        return render(request, 'search.html', {'res': res})


def search(request):
    if request.method == 'POST':
        search_text = request.POST['text']
        res = Phones.objects.filter(name__contains=search_text)
        return render(request, 'search.html', {'res': res})
    else:
        return render(request, 'search.html')


def main(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'user': request.user, 'products': products})


def delete_phone(request, **kwargs):
    phone = Phones.objects.get(id=kwargs['id'])
    phone.delete()
    return redirect('/')

# def home(request):
#     user = User.objects.get(id=1)
#     path = Path('static/images/R.jpg')
#     with path.open(mode='rb') as img:
#         file = File(img, name=img.name)
#     product = Product(name='Apple', user=user, file=file)
#     product.save()
#     product = Product(name='banana', user=user, file=file)
#     product.save()
#     product = Product(name='orange', user=user, file=file)
#     product.save()
#     product = Product(name='tomato', user=user, file=file)
#     product.save()
#     # product.many_user.add(user)
#     # product.save()
#     # product.many_user.add(user)
#     # product.save()
#     # product.many_user.remove(user)
#     # product.save()
#     # print(product.many_user.all())
#     if request.method == 'POST':
#         data = request.POST
#         print(data['text'])
#         name = 'Bob'
#         return redirect('/page2')
#     elif request.method == 'GET':
#         # data = Product.objects.all()  # QuerySet
#         data = Product.objects.filter(id=1)   # QuerySet
#         data[0].name = 'water'
#         data[0].save()
#         data[0].user.username # user object
#         data[0].file  # file object
#         return render(request, 'home.html', {'var': data, 'l': [1, 2, 3, 4]})


def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'], email=form.cleaned_data['email'])
            user.save()
            login(request, user)
            return redirect('/')
    else:
        return render(request, 'registration.html', {'form': Registration(), 'user': request.user})


class RegistrationPage(CreateView):
    template_name = 'registration.html'
    form_class = Registration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def get_success_url(self):
        login(self.request, self.object)
        return '/'


class LoginPage(LoginView):
    template_name = 'registration.html'
    form_class = Login
    redirect_authenticated_user = True


class ProductCreate(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get(self):
        pass

    def post(self, request, *args, **kwargs):
        pass


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(name=form.cleaned_data['name'], user=User.objects.get(id=1))
            product.save()
            return redirect('/')
    else:
        return render(request, 'product_create.html', {'form': ProductForm(), 'user': request.user})


class ProductEdit(UpdateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('home')


# def product_edit(request, **kwargs):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = Product.objects.get(id=kwargs['pk'])
#             product.name = form.cleaned_data['name']
#             product.save()
#             return redirect('/')
#     else:
#         return render(request, 'registration.html', {'form': ProductForm(), 'user': request.user})


class DeleteProduct(DeleteView):
    template_name = 'delete.html'
    model = Product
    success_url = reverse_lazy('home')


# def login_page(request):
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if user:
#                 login(request, user)
#                 return redirect('/')
#     else:
#         return render(request, 'registration.html', {'form': Login()})


class LoginPage(LoginView):
    template_name = 'registration.html'
    form_class = Login
    redirect_authenticated_user = True


class LogoutPage(LogoutView):
    pass


# def logout_page(request):
#     logout(request)
#     return redirect('/')


# def water(request):
#     if request.method == 'POST':
#         data = request.POST
#         return render(request, 'water.html', data)
#     else:
#         form = ComplainForm()
#         return render(request, 'water.html', {'form': form})


class FilmCreate(CreateView):
    template_name = 'registration.html'
    form_class = FilmAdd
    success_url = reverse_lazy('home')


class DirectorCreate(CreateView):
    template_name = 'registration.html'
    form_class = DirectorAdd
    success_url = reverse_lazy('home')


class FilmChange(UpdateView):
    template_name = 'registration.html'
    model = Film
    fields = ['title', 'plot', 'create_date', 'post']
    success_url = reverse_lazy('home')


class DirectorChange(UpdateView):
    template_name = 'registration.html'
    model = Director
    fields = ['name', 'surname']
    success_url = reverse_lazy('home')


class FilmsCatalog(ListView):
    template_name = 'films.html'
    model = Film
    context_object_name = 'films'


class AjaxPage(TemplateView):
    template_name = 'ajax.html'

    def post(self, request):
        data = request.POST
        print(data['text'])
        return JsonResponse({'status': 'OK'}, safe=False)