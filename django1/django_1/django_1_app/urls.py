from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('registration/', views.registration, name='page2'),
    path('water/', views.water),
    path('login/', views.login_page),
    path('logout/', views.logout_page)
]
