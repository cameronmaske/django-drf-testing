from rest_framework import serializers
from journal.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
