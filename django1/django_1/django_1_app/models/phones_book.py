from django.db import models


class Phones(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    comment = models.TextField()

# python manage.py makemigrations
# python manage.py migrate
