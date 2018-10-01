import pytest
from django.urls import reverse

from app.journal.models import Entry


@pytest.fixture
def logged_in_client(client, user):
    client.force_authenticate(user=user)
    return client


def test_list(logged_in_client, entry):
    response = logged_in_client.get(reverse("api:journal:entry-list"), format="json")
    assert response.status_code == 200
    assert response.json() == [
        {"id": entry.id, "text": entry.text, "published": entry.published}
    ]


def test_detail(logged_in_client, entry):
    response = logged_in_client.get(
        reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": entry.id,
        "text": entry.text,
        "published": entry.published,
    }


def test_create(logged_in_client, user):
    text = "Hello World"
    response = logged_in_client.post(
        reverse("api:journal:entry-list"),
        data={"text": text, "published": True},
        format="json",
    )
    assert response.status_code == 201, response.content
    entry = Entry.objects.get()
    assert entry.text == "Hello World"
    assert entry.user == user
    assert response.json() == {"id": entry.id, "text": text, "published": True}


def test_delete(logged_in_client, user, entry):
    response = logged_in_client.delete(
        reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
    )
    assert response.status_code == 204


def test_edit(logged_in_client, user, entry):
    new_text = "Brave new world"
    response = logged_in_client.put(
        reverse("api:journal:entry-detail", args=(entry.id,)),
        data={"text": new_text},
        format="json",
    )
    assert response.status_code == 200, response.content
    entry.refresh_from_db()
    assert entry.text == new_text
