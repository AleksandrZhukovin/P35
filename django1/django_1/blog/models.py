from django.db import models
from django_1_app.models import User


class Post(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
# python manage.py makemigrations
# python manage.py migrate
