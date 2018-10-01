from rest_framework import serializers

from app.journal.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        exclude = ("user",)
