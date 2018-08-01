from django.test import TestCase
from example.models import Example
import pytest

class ExampleTest(TestCase):
    def test_signals_1(self):
        example = Example.objects.create(text="Hello World")
        self.assertEqual(example.text, "Hello World")

    @pytest.mark.enable_signals
    def test_signals_2(self):
        example = Example.objects.create(text="Hello world")
        self.assertEqual(example.text, "Signal override")
