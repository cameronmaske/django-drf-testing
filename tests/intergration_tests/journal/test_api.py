# from datetime import datetime

# import pytest
# import pytz
# from django.urls import reverse

# from app.journal.models import Entry


# @pytest.fixture
# @pytest.mark.django_db
# def entry(user):
#     return Entry.objects.create(
#         user=user,
#         text="It was the best of times, it was the blurst of times.",
#         published=True,
#     )


# @pytest.fixture
# @pytest.mark.django_db
# def logged_in_client(client, user):
#     client.force_authenticate(user=user)
#     return client


# @pytest.mark.django_db
# def test_list_anon(client, entry):
#     response = client.get(reverse("api:journal:entry-list"), format="json")
#     assert response.status_code == 200
#     assert response.json() == [
#         {"id": entry.id, "text": entry.text, "published": entry.published}
#     ]


# @pytest.mark.django_db
# def test_detail_anon(client, entry):
#     response = client.get(
#         reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
#     )
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": entry.id,
#         "text": entry.text,
#         "published": entry.published,
#     }


# @pytest.mark.django_db
# def test_create_anon(client):
#     response = client.post(
#         reverse("api:journal:entry-list"),
#         data={"text": "Hello World", "published": True},
#         format="json",
#     )
#     assert response.status_code == 403


# @pytest.mark.django_db
# def test_delete_anon(client, entry):
#     response = client.delete(
#         reverse("api:journal:entry-detail", args=(entry.id,)), format="json"
#     )
#     assert response.status_code == 403


# @pytest.mark.django_db
# def test_create_user(logged_in_client, user):
#     text = "Hello World"
#     response = logged_in_client.post(
#         reverse("api:journal:entry-list"),
#         data={"text": text, "published": True},
#         format="json",
#     )
#     assert response.status_code == 201, response.content
#     entry = Entry.objects.get()
#     assert entry.text == "Hello World"
#     assert entry.user == user
#     assert response.json() == {"id": entry.id, "text": text, "published": True}
