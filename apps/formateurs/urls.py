from rest_framework.routers import SimpleRouter

from .views import FormateurViewSet

router = SimpleRouter()
router.register("formateurs", FormateurViewSet, basename="formateur")

urlpatterns = router.urls
