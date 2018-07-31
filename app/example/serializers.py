from rest_framework import serializers
from example.models import Example


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ('id', 'text', 'number')
