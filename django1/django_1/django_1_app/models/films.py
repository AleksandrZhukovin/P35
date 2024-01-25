from django.db import models
from .directors import Director


class Film(models.Model):
    title = models.CharField(max_length=100)
    create_date = models.DateField()
    plot = models.TextField()
    # poster = models.ImageField(upload_to='django_1_app/static/images', default='django_1_app/static/images/default.png')
    director = models.ForeignKey(Director, null=True, on_delete=models.SET_NULL)
