from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostsPage.as_view(), name='posts'),
    path('post/<int:id>/', views.PostPage.as_view())
]
