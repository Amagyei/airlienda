# Generated by Django 5.0.3 on 2024-05-27 14:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0003_remove_booking_room_booking_room"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="room",
            new_name="room_id",
        ),
    ]
