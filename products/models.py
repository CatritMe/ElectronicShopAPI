from django.db import models

from suppliers.models import Supplier

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    version = models.CharField(max_length=100, verbose_name='модель', **NULLABLE)
    release_date = models.DateField(verbose_name='дата релиза продукта', **NULLABLE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='поставщик')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
