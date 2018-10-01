from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from app.journal.models import Entry
from app.journal.permissions import AnonCanReadAndUserOrStaffCanCRUD
from app.journal.serializers import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AnonCanReadAndUserOrStaffCanCRUD,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
