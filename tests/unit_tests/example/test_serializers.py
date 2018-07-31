from rest_framework import exceptions
from app.example.serializers import ExampleSerializer
import pytest

def test_1():
    serializer = ExampleSerializer(data={
        'number': 1, 
        'text': "Hello world"
    })
    assert serializer.is_valid()
    assert serializer.data == {
        'number': 1, 
        'text': "Hello world"
    }

def test_2():
    serializer = ExampleSerializer(data={
        'number': 'hello', 
        'text': "Hello world"
    })
    with pytest.raises(exceptions.ValidationError) as exc:
        serializer.is_valid(raise_exception=True)

    assert exc.value.detail == {
        'number': [
            exceptions.ErrorDetail('A valid integer is required.', 'invalid')
        ]
    }
