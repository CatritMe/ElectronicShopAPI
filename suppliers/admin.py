from django.contrib import admin
from django.utils.html import format_html

from suppliers.models import Supplier, Contact


@admin.action(description="Обнулить задолженность перед поставщиком")
def reset_debts(queryset):
    """
    Добавление admin action для обнуления задолженности выбранных поставщиков
    """
    queryset.update(debts=0)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Отображение поставщиков в админке
    """

    list_display = ("id", "name", "to_parent_supplier", "debts", "city")
    list_filter = ("contact__city",)
    actions = [reset_debts]

    @staticmethod
    def to_parent_supplier(obj: Supplier):
        """
        создание ссылки на поставщика
        """
        if obj.parent_supplier is not None:
            return format_html(
                '<a href="/admin/suppliers/{id}/">{name}</a>',
                id=obj.parent_supplier.pk,
                name=obj.parent_supplier.name,
            )

    @staticmethod
    def city(obj: Supplier):
        """
        добавление поля "city" из привязанных к поставщику контактов
        """
        return Contact.objects.get(supplier=obj).city


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Отображение контактов в админке
    """

    list_display = (
        "id",
        "email",
        "country",
    )
