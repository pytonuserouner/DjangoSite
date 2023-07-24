# Generated by Django 4.2.3 on 2023-07-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0003_profile_balance_alter_avataruser_src_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="balance",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0,
                max_digits=12,
                verbose_name="баланс",
            ),
        ),
    ]
