# Generated by Django 5.0.3 on 2024-05-07 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomtype",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
