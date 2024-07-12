# Generated by Django 5.0.3 on 2024-06-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0007_alter_booking_booking_id_alter_booking_success_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("paid", "Paid"),
                    ("pending", "Pending"),
                    ("processing", "Processing"),
                    ("cancelled", "Cancelled"),
                    ("initiated", "Initiated"),
                    ("failed", "Failed"),
                    ("refunding", "Refunding"),
                    ("refunded", "Refunded"),
                    ("unpaid", "Unpaid"),
                    ("expired", "Expired"),
                ],
                max_length=100,
            ),
        ),
    ]