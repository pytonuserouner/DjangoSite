# Generated by Django 4.2.2 on 2023-06-23 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products_app", "0002_product_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("createdAt", models.DateTimeField(blank=True, verbose_name="дата")),
                (
                    "fullName",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="полное имя"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="электронная почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="телефон"
                    ),
                ),
                (
                    "deliveryType",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="тип доставки"
                    ),
                ),
                (
                    "paymentType",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="тип оплаты"
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        max_digits=11,
                        verbose_name="общая сумма",
                    ),
                ),
                (
                    "status",
                    models.CharField(blank=True, max_length=255, verbose_name="статус"),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=255, verbose_name="город"),
                ),
                (
                    "address",
                    models.CharField(blank=True, max_length=255, verbose_name="адрес"),
                ),
                (
                    "products",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products_app.product",
                        verbose_name="список продуктов",
                    ),
                ),
            ],
        ),
    ]