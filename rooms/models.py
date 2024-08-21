#rooms/model.py
from django.db import models
from hostel.models import Hostel
from django.utils.text import slugify
from shortuuid.django_fields import ShortUUIDField
import shortuuid 

from userauth.models import User

ROOM_STATUS = (
    ('OCCUPIED', "OCCUPIED"),
    ('VACANT', 'VACANT')
)





# Create your models here.

class RoomType(models.Model):
    hostel= models.ForeignKey(Hostel, on_delete= models.CASCADE)
    name= models.CharField(max_length=100)
    residents = models.IntegerField(max_length=1, verbose_name=("Number of Residents/Beds"))
    room_size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=("Room Size"))
    balcony_size = models.DecimalField( max_digits=10, decimal_places=2, verbose_name=("Balcony Size"))
    price = models.DecimalField( max_digits=8, decimal_places=2)
    amenities = models.CharField(max_length=200, help_text="seperate tags with comma", null=True, blank=True)
    rtid = ShortUUIDField(unique = True, length = 5, max_length=6,alphabet="abcde12345")
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='roomtype_images/', default='default.jpg')

    def __str__(self):
        return f'{self.name} - {self.hostel.name} - {self.price}'
    
    def rooms_count (self):
        Room.objects.filter(room_type=self).count()
        
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
    rid = ShortUUIDField(unique=True, length=5, max_length=6, alphabet="abcde12345")
    slug = models.SlugField()
    status = models.CharField(choices=ROOM_STATUS, max_length=20, default="VACANT")
    current_occupants = models.ManyToManyField(User, blank=True, related_name='rooms')

    @property
    def is_full(self):
        """Check if the room has reached its capacity of residents."""
        return self.current_occupants.count() >= self.type.residents

    def save(self, *args, **kwargs):
        if not self.slug:
            uuid_key = shortuuid.uuid()
            unique_id = uuid_key[:4]
            self.slug = slugify(f'{self.type}-{self.number}-{unique_id.lower()}')
        super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.type} - {self.hostel.name} - Room {self.number}'

    class Meta:
        verbose_name_plural = "Rooms"
        unique_together = (('number', 'hostel'), ('slug', 'hostel'))

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            uuid_key = shortuuid.uuid()
            unique_slug_part = uuid_key[:2]
            self.slug = slugify(f'{self.name}-{unique_slug_part}')
        super(InventoryItem, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity})"

    class Meta:
        verbose_name_plural = "Inventory Items"
        ordering = ['name']

class InventoryList(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name='inventory_lists')
    items = models.ManyToManyField(InventoryItem, related_name='inventory_lists')
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        item_names = ', '.join([item.name for item in self.items.all()])
        return f"Inventory List for {self.room_type.name}: {item_names}"

    class Meta:
        verbose_name_plural = "Inventory Lists"
        unique_together = ('room_type',)  