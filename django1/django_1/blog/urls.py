from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsPage.as_view()),
    path('post/<int:id>/', views.PostPage.as_view())
]
