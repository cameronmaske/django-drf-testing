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


@pytest.mark.django_db# Simulate many tests
def test_1(client):
    test_create(client)

@pytest.mark.django_db
def test_2(client):
    test_create(client)

@pytest.mark.django_db
def test_3(client):
    test_create(client)

@pytest.mark.django_db
def test_4(client):
    test_create(client)

@pytest.mark.django_db
def test_5(client):
    test_create(client)

@pytest.mark.django_db
def test_6(client):
    test_create(client)

@pytest.mark.django_db
def test_7(client):
    test_create(client)

@pytest.mark.django_db
def test_8(client):
    test_create(client)

@pytest.mark.django_db
def test_9(client):
    test_create(client)

@pytest.mark.django_db
def test_10(client):
    test_create(client)