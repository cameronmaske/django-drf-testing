import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(autouse=True)
def enable_db_access_for_all_intergration_tests(db):
    pass


@pytest.fixture
@pytest.mark.django_db
def user():
    User = get_user_model()
    return User.objects.create(
        email="john@example.com", username="johndoe", is_staff=False
    )


@pytest.fixture
@pytest.mark.django_db
def staff():
    User = get_user_model()
    return User.objects.create(email="alice@staff.com", username="alice", is_staff=True)
