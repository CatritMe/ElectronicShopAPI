from rest_framework.viewsets import ModelViewSet

from suppliers.models import Supplier, Contact
from suppliers.serializers import SupplierSerializer, SupplierCreateSerializer
from users.permissions import IsActiveUser


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    filterset_fields = ("contact__country",)
    permission_classes = (IsActiveUser,)

    def perform_create(self, serializer):
        """при создании поставщика присваивать уровень в зависимости от родителя-поставщика"""
        supplier = serializer.save()
        if supplier.type == "завод":
            supplier.level = 0
        if supplier.parent_supplier:
            if supplier.parent_supplier.type == "завод":
                supplier.level = 1
            else:
                supplier.level = 2
        supplier.save()

    def get_serializer_class(self):
        if self.action == "create":
            return SupplierCreateSerializer
        else:
            return SupplierSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = (IsActiveUser,)
