from rest_framework.routers import DefaultRouter

from content.api.v1.views import ArchivoViewSet

router = DefaultRouter()
router.register(r'archivos', ArchivoViewSet, basename='user')
urlpatterns = router.urls
