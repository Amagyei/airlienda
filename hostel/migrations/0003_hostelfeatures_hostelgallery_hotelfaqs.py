# Generated by Django 5.0.3 on 2024-05-04 15:59

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hostel", "0002_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HostelFeatures",
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
                    "icon_type",
                    models.CharField(
                        choices=[
                            ("Bootstrap Icons", "Bootstrap Icons"),
                            ("Fontawesome Icons", "Fontawesome Icons"),
                            ("Box Icons", "Remi Icons"),
                            ("Flat Icons", "Flat Icons"),
                        ],
                        max_length=100,
                        null=True,
                    ),
                ),
                ("icon", models.CharField(blank=True, max_length=100, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Hostel Features",
            },
        ),
        migrations.CreateModel(
            name="HostelGallery",
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
                ("image", models.FileField(upload_to="hostel_gallery")),
                (
                    "hgid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcdefghijklmnopqrstuvwxyz",
                        length=10,
                        max_length=20,
                        prefix="",
                        unique=True,
                    ),
                ),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Hostel Gallery",
            },
        ),
        migrations.CreateModel(
            name="HotelFaqs",
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
                ("question", models.CharField(max_length=1000)),
                ("answer", models.CharField(blank=True, max_length=1000, null=True)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Hotel FAQs",
            },
        ),
    ]
