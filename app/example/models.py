from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Example(models.Model):
    text = models.CharField(max_length=500)


@receiver(pre_save, sender=Example)
def pre_save_signal(sender, instance, **kwargs):
    instance.text = "Signal override"