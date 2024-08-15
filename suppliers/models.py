from django.db import models

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name="название")
    # email = models.EmailField(verbose_name="email")
    # country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)
    # city = models.CharField(max_length=100, verbose_name="город", **NULLABLE)
    # street = models.CharField(max_length=100, verbose_name="улица", **NULLABLE)
    # house = models.CharField(max_length=100, verbose_name="номер дома", **NULLABLE)
    parent_supplier = models.ForeignKey(
        "self", on_delete=models.CASCADE, verbose_name="поставщик", **NULLABLE
    )
    debts = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        default=None,
        verbose_name="задолженность перед поставщиком",
        **NULLABLE
    )
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="время создания")

    FACTORY = "завод"
    RETAIL = "розничная сеть"
    SHOP = "индивидуальный предприниматель"
    types = [
        (FACTORY, "завод"),
        (RETAIL, "розничная сеть"),
        (SHOP, "индивидуальный предприниматель"),
    ]
    type = models.CharField(
        max_length=30, choices=types, default=SHOP, verbose_name="тип предприятия"
    )
    level = models.SmallIntegerField(verbose_name="уровень", default=0)

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


class Contact(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, verbose_name="поставщик"
    )
    email = models.EmailField(verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="город", **NULLABLE)
    street = models.CharField(max_length=100, verbose_name="улица", **NULLABLE)
    house = models.CharField(max_length=100, verbose_name="номер дома", **NULLABLE)

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return self.email
