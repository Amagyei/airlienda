#rooms/model.py
from django.db import models
from hostel.models import Hostel
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid 

ROOM_STATUS = (
    ('OCCUPIED', "OCCUPIED"),
    ('VACANT', 'VACANT')
)

 



# Create your models here.

class RoomType(models.Model):
    hostel= models.ForeignKey(Hostel, on_delete= models.CASCADE)
    name= models.CharField(max_length=100)
    residents = models.IntegerField(max_length=1, verbose_name=("Number of Residents"))
    room_size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("Room Size"))
    balcony_size = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=("Balcony Size"))
    price = models.DecimalField( max_digits=8, decimal_places=2)
    amenities = models.CharField(max_length=200, help_text="seperate tags with comma", null=True, blank=True)
    rtid = ShortUUIDField(unique = True, length = 5, max_length=6,alphabet="abcde12345")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.name} - {self.hostel.name} - {self.price}'
    
    def rooms_count (self):
        Room.objects.filter(room_type=self)-count()
        
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuiduuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' + str(uniqueid.lower())
        super (RoomType, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Room Types"

class Room(models.Model):
    type = models.ForeignKey(RoomType, verbose_name="Room Type", on_delete=models.CASCADE)
    number = models.IntegerField(verbose_name="Room Number")
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    residents = models.CharField(max_length=1000, null=True, blank=True)
    rid = ShortUUIDField(unique=True, length=5, max_length=6, alphabet="abcde12345")
    slug = models.SlugField()
    status = models.CharField(choices=ROOM_STATUS, max_length=20, default="VACANT")

    def __str__(self):
        return f'{self.type} - {self.hostel.name} - Room {self.number}'

    def save(self, *args, **kwargs):
        if not self.slug:
            uuid_key = shortuuid.uuid()  # Fixed function name
            unique_id = uuid_key[:4]
            self.slug = slugify(f'{self.type}-{self.number}-{unique_id.lower()}')
        super(Room, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Rooms"
        unique_together = (('number', 'hostel'), ('slug', 'hostel'))  # Ensure uniqueness of number and slug within each hostel



