from django.db import models


class Abstract(models.Model):
    modified_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True
