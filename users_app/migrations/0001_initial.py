# Generated by Django 4.2.2 on 2023-06-15 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users_app.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="AvatarUser",
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
                (
                    "src",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=users_app.models.profile_avatar_directory_path,
                        verbose_name="синий внеземлянин",
                    ),
                ),
                (
                    "alt",
                    models.CharField(
                        blank=True,
                        max_length=500,
                        verbose_name="альтернатива синему внеземлянину",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                (
                    "fullName",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="полное имя"
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="электронная почта"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="телефон"
                    ),
                ),
                (
                    "avatar",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users_app.avataruser",
                        verbose_name="синий внеземлянин",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]