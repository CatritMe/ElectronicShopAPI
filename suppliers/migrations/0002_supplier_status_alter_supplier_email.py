# Generated by Django 5.1 on 2024-08-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="supplier",
            name="status",
            field=models.CharField(
                choices=[
                    ("завод", "завод"),
                    ("розничная сеть", "розничная сеть"),
                    (
                        "индивидуальный предприниматель",
                        "индивидуальный предприниматель",
                    ),
                ],
                default="индивидуальный предприниматель",
                max_length=30,
                verbose_name="тип предприятия",
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="email"),
        ),
    ]
