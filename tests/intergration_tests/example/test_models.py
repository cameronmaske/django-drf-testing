import pytest
from example.models import Example

@pytest.mark.django_db
def test_signals_disabled():
    example = Example.objects.create(text="Hello World")
    assert example.text == "Hello World"

@pytest.mark.django_db
@pytest.mark.enable_signals
def test_signals_enabled():
    example = Example.objects.create(text="Hello world")
    assert example.text == "Signal override"

