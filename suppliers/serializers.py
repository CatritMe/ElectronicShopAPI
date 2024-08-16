from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from products.models import Product
from suppliers.models import Supplier, Contact


class SupplierSerializer(ModelSerializer):
    """
    Сериалайзер для поставщика для всех действий, кроме создания нового
    """
    products = SerializerMethodField()
    debts = serializers.DecimalField(read_only=True, max_digits=20, decimal_places=2)
    parent_supplier = SerializerMethodField()
    email = SerializerMethodField()
    country = SerializerMethodField()
    city = SerializerMethodField()
    street = SerializerMethodField()
    house = SerializerMethodField()

    @staticmethod
    def get_products(supplier):
        """
        Получение списка продуктов поставщика
        """
        return [product.name for product in Product.objects.filter(supplier=supplier)]

    @staticmethod
    def get_parent_supplier(supplier):
        """
        Получение названия родительского поставщика
        """
        if supplier.parent_supplier:
            return supplier.parent_supplier.name

    @staticmethod
    def get_email(supplier):
        """
        Получение email из привязанных контактов
        """
        return Contact.objects.get(supplier=supplier).email

    @staticmethod
    def get_country(supplier):
        """
        Получение страны из привязанных контактов
        """
        return Contact.objects.get(supplier=supplier).country

    @staticmethod
    def get_city(supplier):
        """
        Получение города из привязанных контактов
        """
        return Contact.objects.get(supplier=supplier).city

    @staticmethod
    def get_street(supplier):
        """
        Получение улицы из привязанных контактов
        """
        return Contact.objects.get(supplier=supplier).street

    @staticmethod
    def get_house(supplier):
        """
        Получение номера дома из привязанных контактов
        """
        return Contact.objects.get(supplier=supplier).house

    class Meta:
        model = Supplier
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    """
    Сериалайзер для контактов
    """
    class Meta:
        model = Contact
        fields = "__all__"


class SupplierCreateSerializer(ModelSerializer):
    """
    Сериалайзер для поставщика для действия "create"
    """
    supplier = serializers.SlugRelatedField(
        required=False, queryset=Supplier.objects.all(), slug_field="name"
    )
    contact = ContactSerializer(required=False)

    class Meta:
        model = Supplier
        exclude = ("level",)

    def is_valid(self, *, raise_exception=False):
        self._contact = self.initial_data.pop("contact", {})
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        supplier = Supplier.objects.create(**validated_data)
        supplier.save()

        contact = Contact.objects.create(
            supplier=supplier,
            email=self._contact.get("email", None),
            country=self._contact.get("country", None),
            city=self._contact.get("city", None),
            street=self._contact.get("street", None),
            house=self._contact.get("house", None),
        )
        contact.save()
        return supplier
