from django.urls import reverse
import pytest 
from example.models import Example


@pytest.mark.django_db
def test_list_empty(client):
    response = client.get("/api/example/", format='json')
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_create(client):
    response = client.post("/api/example/", data={'number': 2, 'text': "Hello World"}, format='json')
    assert response.status_code == 201
    example = Example.objects.get()
    assert example.number == 2 
    assert example.text == "Hello World"
    assert response.json() == {
        'id': example.id,
        'number': 2,
        'text': "Hello World"
    }
