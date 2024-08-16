from rest_framework.routers import SimpleRouter

from suppliers.apps import SuppliersConfig
from suppliers.views import SupplierViewSet, ContactViewSet

app_name = SuppliersConfig.name

router = SimpleRouter()
router.register("", SupplierViewSet)

urlpatterns = []

urlpatterns += router.urls
