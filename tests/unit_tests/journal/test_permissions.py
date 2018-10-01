from unittest import mock

import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

from app.journal.permissions import AnonCanReadAndUserOrStaffCanCRUD

permission = AnonCanReadAndUserOrStaffCanCRUD()


@pytest.fixture
def anon_request():
    return mock.Mock(user=AnonymousUser())


@pytest.fixture
def user():
    User = get_user_model()
    return User()


@pytest.fixture
def user_request(user):
    return mock.Mock(user=user)


@pytest.fixture
def staff_request(user):
    return mock.Mock(user=get_user_model()(is_staff=True))


@pytest.fixture
def instance(user):
    return mock.Mock(user=user)


@pytest.mark.parametrize(
    # fmt: off
    "action,expected", [
        ("list", True), 
        ("retrieve", True), 
        ("create", False)
    ]  # fmt: on
)
def test_anon_has_permission(action, expected, anon_request):
    view = mock.Mock(action=action)
    assert permission.has_permission(anon_request, view) is expected


def test_user_has_permission(user_request):
    view = mock.Mock(action="create")
    assert permission.has_permission(user_request, view) is True


@pytest.mark.parametrize(
    # fmt: off
    "action,expected", [
        ("retrieve", True),
        ("list", False),
        ("create", False)
    ]  # fmt: on
)
def test_anon_has_object_permission_retrieve(action, expected, anon_request, instance):
    view = mock.Mock(action=action)
    assert permission.has_object_permission(anon_request, view, instance) is expected


def test_user_has_object_permission_owner(user_request, instance):
    view = mock.Mock(action="*")
    assert permission.has_object_permission(user_request, view, instance) is True


def test_others_user_has_object_permission_owner(user_request, instance):
    other_users_instance = mock.Mock(user=get_user_model()())
    view = mock.Mock(action="*")
    assert (
        permission.has_object_permission(user_request, view, other_users_instance)
        is False
    )


def test_staff_has_object_permission_owner_create(staff_request, instance):
    view = mock.Mock(action="create")
    assert permission.has_object_permission(staff_request, view, instance) is False
