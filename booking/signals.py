from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Booking
from rooms.models import Room

@receiver(post_save, sender=Booking)
def auto_update_room_status(sender, instance, **kwargs):
    if instance.payment_status == "paid":  # Assuming 'paid' triggers the update
        room = Room.objects.get(rid=instance.room_id)
        if room.status != "OCCUPIED":
            room.status = 'OCCUPIED'
            room.save()
            print(f'Room {room.number} updated to OCCUPIED due to booking confirmation.')