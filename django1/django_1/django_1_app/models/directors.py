from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
