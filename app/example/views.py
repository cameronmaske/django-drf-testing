from rest_framework import viewsets
from example.models import Example
from example.serializers import ExampleSerializer

class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
