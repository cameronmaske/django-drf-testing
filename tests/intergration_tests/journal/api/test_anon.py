from django.urls import reverse

from app.journal.models import Entry


def test_list(client, entry):
    response = client.get(reverse("api:journal:entry-list"), format="json")
    assert response.status_code == 200
    assert response.json() == [
        {"id": entry.id, "text": entry.text, "published": entry.published}
    ]


def test_detail(client, entry):
    response = client.get(
        reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": entry.id,
        "text": entry.text,
        "published": entry.published,
    }


def test_create(client):
    response = client.post(
        reverse("api:journal:entry-list"),
        data={"text": "Hello World", "published": True},
        format="json",
    )
    assert response.status_code == 403


def test_delete(client, entry):
    response = client.delete(
        reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
    )
    assert response.status_code == 403
