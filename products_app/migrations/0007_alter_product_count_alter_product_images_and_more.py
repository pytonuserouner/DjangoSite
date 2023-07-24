# Generated by Django 4.2.3 on 2023-07-06 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0006_delete_catalog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="count",
            field=models.IntegerField(default=0, verbose_name="количество"),
        ),
        migrations.AlterField(
            model_name="product",
            name="images",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products_app.productimage",
                verbose_name="изображения продукта",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="tags",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="products_app.tags",
                verbose_name="тэги",
            ),
        ),
    ]
