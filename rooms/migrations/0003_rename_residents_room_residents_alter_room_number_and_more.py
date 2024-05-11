# Generated by Django 5.0.3 on 2024-05-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hostel", "0004_alter_hostel_description"),
        ("rooms", "0002_alter_roomtype_price"),
    ]

    operations = [
        migrations.RenameField(
            model_name="room",
            old_name="Residents",
            new_name="residents",
        ),
        migrations.AlterField(
            model_name="room",
            name="number",
            field=models.IntegerField(verbose_name="Room Number"),
        ),
        migrations.AlterField(
            model_name="room",
            name="slug",
            field=models.SlugField(),
        ),
        migrations.AlterUniqueTogether(
            name="room",
            unique_together={("number", "hostel"), ("slug", "hostel")},
        ),
    ]