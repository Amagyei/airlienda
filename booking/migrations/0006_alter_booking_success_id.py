# Generated by Django 5.0.3 on 2024-05-28 15:24

import shortuuid.django_fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0005_alter_booking_room_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="success_id",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet=" abcdefghijkImnopqrstuvwxyz",
                blank=True,
                length=10,
                max_length=20,
                null=True,
                prefix="",
            ),
        ),
    ]
