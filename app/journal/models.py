from django.conf import settings
from django.db import models


class Entry(models.Model):
    text = models.TextField()
    published = models.BooleanField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
