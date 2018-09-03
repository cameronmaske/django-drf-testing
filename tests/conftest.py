import os
import pytest 
from django.conf import settings

@pytest.fixture(scope='session')
def django_db_modify_db_settings(request):
    settings.DATABASES = {
        'default': {
            'ENGINE':'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }
    