from app.api.routers import Router
from app.journal.views import EntryViewSet

router = Router()
router.register(r"entries", EntryViewSet)
