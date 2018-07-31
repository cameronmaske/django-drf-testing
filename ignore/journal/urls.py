from rest_framework import routers
from journal.views import EntryViewSet 

router = routers.SimpleRouter()
router.register(r'entries', EntryViewSet)
