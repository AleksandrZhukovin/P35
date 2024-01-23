from django.db import models
from .abstract import Abstract
from . import User


class Product(Abstract):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # many_user = models.ManyToManyField(User, related_name='many_user')
    # image = models.ImageField(upload_to='django_1_app/static/images')
    # price = models.FloatField()
    # fiels = models.OneToOneField(User, on_delete=models.CASCADE)
    # field1 = models.ForeignKey(User, on_delete=models.CASCADE)
    # field2 = models.ManyToManyField(User)
    # file = models.FileField()
