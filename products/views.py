from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers import ProductSerializer
from users.permissions import IsActiveUser


class ProductViewSet(ModelViewSet):
    """
    Вьюсет для CRUD продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsActiveUser,)
