from django.db import models
from hostel.models import Hostel
from rooms.models import Room, RoomType
from userauth.models import User
from shortuuid.django_fields import ShortUUIDField
 
PAYMENT_STATUS = (
    ("paid", "Paid"), 
    ("pending", "Pending"), 
    ("Processing", "Processing"), 
    ("cancelled", "cancelled"), 
    ("initiated", "initiated"), 
    ("failed", "failed"), 
    ("refunding", "refunding"),
    ("refunded", "refunded"),
    ("unpaid", "Unpaid"),
    ("expired", "expired")
)

# Create your models here.

class Booking (models.Model):
    user = models.ForeignKey (User, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.CharField (max_length=100, choices=PAYMENT_STATUS)
    full_name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    phone = models.CharField(max_length=1000)
    hostel = models.ForeignKey (Hostel, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    room_id = models.CharField(max_length=1000, null=True, blank=True)
    before_discount = models.DecimalField (max_digits=12, decimal_places=2, default=0.00)
    total = models.DecimalField (max_digits=12, decimal_places=2, default=0.00)
    saved = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=100, null=True, blank=True)
    success_id = ShortUUIDField(length=10, max_length=20, alphabet="abcdefghijkImnopqrstuvwxyz", null=True, blank=True)
    booking_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijkImnopqrstuvwxyz")
    
    def __str__(self):
        return f"{self.booking_id}"
    
    def rooms (self):
        return self.room.all().count()


