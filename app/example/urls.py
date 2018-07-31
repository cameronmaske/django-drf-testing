from rest_framework import routers
from example.views import ExampleViewSet 

router = routers.SimpleRouter()
router.register(r'example', ExampleViewSet)
