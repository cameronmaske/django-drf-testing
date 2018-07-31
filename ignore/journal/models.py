from django.conf import settings
from django.db import models


class Entry(models.Model):
    text = models.TextField()
    timestamp = models.DatetimeField()
    # Instead of refer to User, or get_user_model, for Foreign keys you should use the AUTH_USER_MODEL setting instead
    # See: https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#django.contrib.auth.get_user_model
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    