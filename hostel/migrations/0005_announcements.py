# Generated by Django 5.0.3 on 2024-07-12 07:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hostel", "0004_alter_hostel_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcements",
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
                ("title", models.CharField(max_length=100)),
                ("date", models.DateTimeField(auto_now_add=True)),
                (
                    "hostel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="hostel.hostel"
                    ),
                ),
            ],
        ),
    ]