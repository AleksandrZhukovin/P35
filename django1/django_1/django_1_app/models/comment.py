from django.db import models
from .news import News
from .user import User


class Comment(models.Model):
    text = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
