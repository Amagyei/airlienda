from django.db import models
from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs

from userauth.models import User
# Create your models here.

class complaint(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('under_review', 'Under Review'),
        ('fixed', 'Fixed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    room_number= models.CharField(max_length=255, null=True, blank=True, verbose_name="Room Number")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    date_completed = models.DateTimeField(null=True, blank=True, verbose_name="Date Completed")
    title = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f"{self.title} - {self.status} - {self.room_number}"

# Create your models here.
