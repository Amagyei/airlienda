
from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from userauth.models import User
import shortuuid 
from shortuuid.django_fields import ShortUUIDField
from django_ckeditor_5.fields import CKEditor5Field


HOSTEL_STATUS = (
    ("Draft", "Draft"),
    ("Disabled","Disabled"),
    ("Rejected", "Rejected"),
    ("In Review", "Draft"),
    ("Live", "Live"),
)
ICON_TYPE =(
    ("Bootstrap Icons", "Bootstrap Icons"),
    ("Fontawesome Icons", "Fontawesome Icons"),
    ("Box Icons", "Remi Icons"),
    ("Flat Icons", "Flat Icons")
 )
    


# Create your models here.
class Hostel(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    description = CKEditor5Field(null=True, blank=True)
    image = models.FileField(upload_to="hostel_gallery")
    address = models.CharField(max_length=150)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    status = models.CharField(max_length=20, choices= HOSTEL_STATUS, default="Live")
    tags = models.CharField(max_length=200, help_text="seperate tags with comma ") 
    views = models.IntegerField(default=0)
    features = models.BooleanField(default=False)
    hid = ShortUUIDField(unique = True, length = 10, max_length=20,alphabet="abcdefghijklmnopqrstuvwxyz")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        if self.slug == "" or self.slug is None :
            uuid_key = shortuuid.uuid()
            unique_id = uuid_key[:4]
            self.slug = slugify(self.name) +'-' + str(unique_id.lower())
        
        super(Hostel, self).save(* args, **kwargs)
        
    def thumbnail(self):
        return mark_safe("<img src='%s' width='50' height = '50px' style='object-fit: cover; border-radius: 6px;'/>" % (self.image.url)) 


class HostelGallery(models.Model):
    hostel = models.ForeignKey(Hostel , on_delete= models.CASCADE)
    image =  models.FileField(upload_to="hostel_gallery")
    hgid = ShortUUIDField(unique = True, length= 10, max_length=20, alphabet = "abcdefghijklmnopqrstuvwxyz")

    def __str__(self):
        return str (self.hostel.name)
    
    class Meta:
        verbose_name_plural = "Hostel Gallery"

class HostelFeatures(models.Model):
    hostel = models.ForeignKey(Hostel , on_delete= models.CASCADE)
    icon_type = models.CharField(max_length=100, null=True, choices=ICON_TYPE)
    icon =  models.CharField(max_length=100, null = True, blank=True)
    name =  models.CharField(max_length=100, null = True, blank=True)

    def __str__(self):
        return str (self.name)
    
    class Meta:
        verbose_name_plural = "Hostel Features"

class HotelFaqs (models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models. CASCADE)
    question = models. CharField(max_length=1000)
    answer = models. CharField (max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def str (self):
        return str(self.question)
    class Meta:
        verbose_name_plural = "Hotel FAQs"


class Announcements(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return str(self.title)
