import os
import django
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'app.config.settings'
django.setup()


def pytest_configure():
    settings.DEBUG = False