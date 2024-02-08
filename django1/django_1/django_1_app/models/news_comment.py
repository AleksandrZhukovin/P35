from django.db import models
from .user import User
from .news import News


class CommentNews(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

# python manage.py makemigrations
# python manage.py migrate
