from django.conf import settings
from django.db import models


class Example(models.Model):
    text = models.CharField(max_length=500)
    number = models.IntegerField()

    