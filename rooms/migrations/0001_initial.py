# Generated by Django 5.0.3 on 2024-05-05 03:12

import django.db.models.deletion
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("hostel", "0003_hostelfeatures_hostelgallery_hotelfaqs"),
    ]

    operations = [
        migrations.CreateModel(
            name="RoomType",
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
                ("name", models.CharField(max_length=100)),
                (
                    "residents",
                    models.IntegerField(
                        max_length=1, verbose_name="Number of Residents"
                    ),
                ),
                (
                    "room_size",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Room Size"
                    ),
                ),
                (
                    "balcony_size",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Balcony Size"
                    ),
                ),
                ("price", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "amenities",
                    models.CharField(
                        blank=True,
                        help_text="seperate tags with comma",
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "rtid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcde12345",
                        length=5,
                        max_length=6,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Room Types",
            },
        ),
        migrations.CreateModel(
            name="Room",
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
                    "number",
                    models.IntegerField(
                        max_length=4, unique=True, verbose_name="Room Number"
                    ),
                ),
                ("Residents", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "rid",
                    shortuuid.django_fields.ShortUUIDField(
                        alphabet="abcde12345",
                        length=5,
                        max_length=6,
                        prefix="",
                        unique=True,
                    ),
                ),
                ("slug", models.SlugField(unique=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("OCCUPIED", "OCCUPIED"), ("VACANT", "VACANT")],
                        default="VACANT",
                        max_length=20,
                    ),
                ),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rooms.roomtype",
                        verbose_name="Room Type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Rooms",
            },
        ),
    ]
