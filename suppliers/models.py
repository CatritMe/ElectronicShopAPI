from django.db import models

NULLABLE = {"blank": True, "null": True}


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(unique=True, verbose_name="email")
    country = models.CharField(max_length=100, verbose_name="страна", **NULLABLE)
    city = models.CharField(max_length=100, verbose_name="город", **NULLABLE)
    street = models.CharField(max_length=100, verbose_name="улица", **NULLABLE)
    house = models.CharField(max_length=100, verbose_name="номер дома", **NULLABLE)
    parent_supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="поставщик", **NULLABLE)
    debts = models.IntegerField(default=0, verbose_name='задолженность перед поставщиком')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name
