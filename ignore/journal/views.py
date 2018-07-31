from rest_framework import viewsets
from journal.models import Entry
from journal.serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
