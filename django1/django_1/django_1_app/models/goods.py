from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField(upload_to='static/images')

    # python manage.py makemigrations
    # python manage.py migrate
