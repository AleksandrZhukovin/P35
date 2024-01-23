from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.HomePage.as_view()), name='home'),
    path('registration/', views.RegistrationPage.as_view(), name='page2'),
    path('login/', views.LoginPage.as_view()),
    path('logout/', views.LogoutPage.as_view()),
    path('product_create/', views.ProductCreate.as_view()),
    path('edit_product/<int:pk>/', views.ProductEdit.as_view()),
    path('delete/<int:pk>/', views.DeleteProduct.as_view()),
    path('film_create/', views.FilmCreate.as_view()),
    path('director_create/', views.DirectorCreate.as_view()),
    path('film_change/<int:pk>/', views.FilmChange.as_view()),
    path('director_change/<int:pk>/', views.DirectorChange.as_view())
]
