# Generated by Django 4.2.2 on 2023-06-23 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="title",
            field=models.CharField(
                max_length=255, null=True, verbose_name="название категории"
            ),
        ),
    ]
