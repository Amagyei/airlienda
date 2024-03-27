# Generated by Django 5.0.3 on 2024-03-27 05:28

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
import userauth.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=156, null=True)),
                ("username", models.CharField(max_length=156, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phone",
                    models.CharField(blank=True, max_length=16, null=True, unique=True),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("1", "Male"), ("2", "Female")],
                        default="other",
                        max_length=20,
                    ),
                ),
                ("otp", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
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
                    "pid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvwxyz1234567890 ",
                        length=8,
                        max_length=25,
                        prefix="",
                        unique=True,
                    ),
                ),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        default="default.jpg",
                        null=True,
                        upload_to=userauth.models.user_dir_path,
                    ),
                ),
                ("full_name", models.CharField(blank=True, max_length=156, null=True)),
                (
                    "phone",
                    models.CharField(blank=True, max_length=16, null=True, unique=True),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("1", "Male"), ("2", "Female")],
                        default="other",
                        max_length=20,
                    ),
                ),
                (
                    "residential_address",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "mailing_address",
                    models.CharField(blank=True, max_length=156, null=True),
                ),
                (
                    "parents_name",
                    models.CharField(blank=True, max_length=156, null=True),
                ),
                (
                    "parents_number",
                    models.CharField(blank=True, max_length=156, null=True),
                ),
                (
                    "id_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("GH_CARD", "Ghana Card"),
                            ("DL", "Driver's License"),
                            ("PASSPORT", "Passport"),
                        ],
                        default="other",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "id_card_number",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("verified", models.BooleanField(default=False)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-date"],
            },
        ),
    ]
