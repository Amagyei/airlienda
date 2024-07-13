from django.db import models
from django.contrib.auth.models import AbstractUser
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save

GENDER = (
    ("1", "Male"),
    ("2", "Female")
)

ID_CARD_TYPE = (
    ('GH_CARD', "Ghana Card"),
    ("DL", "Driver's License"),
    ("PASSPORT", "Passport"),
)

def user_dir_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=156, null = True, blank = True)
    username = models.CharField(max_length=156, unique= True)
    email = models.EmailField(unique= True)
    phone = models.CharField(max_length = 16, null = True, blank = True, unique= True)
    gender = models.CharField(max_length=20, choices = GENDER, default = "other")
    otp = models.CharField(max_length = 100, null = True, blank = True)
    uid = ShortUUIDField(length = 8, max_length = 25, unique = True,  primary_key=True, alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890')
    type = models.CharField(max_length=156, null = True, blank = True)



    USERNAME_FIELD =  'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    # class Meta:
    #     swappable = 'AUTH_USER_MODEL'


class Profile(models.Model):
    image = models.FileField(upload_to=user_dir_path, default="default.jpg", null = True, blank=True )
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    full_name = models.CharField(max_length=156, null = True, blank = True) 
    phone = models.CharField(max_length = 16, null = True, blank = True, unique= True)
    gender = models.CharField(max_length=20, choices = GENDER, default = "other")
    residential_address = models.CharField(max_length=256, null = True, blank = True)
    mailing_address = models.CharField(max_length=156, null = True, blank = True)
    parents_name = models.CharField(max_length=156, null = True, blank = True)
    parents_number = models.CharField(max_length=156, null = True, blank = True)
    id_type =  models.CharField(max_length=50, choices = ID_CARD_TYPE, default = "other", null = True, blank = True)
    id_card_number = models.CharField(max_length = 50, null = True, blank = True )
    verified = models.BooleanField( default = False)
    date = models.DateTimeField(auto_now_add = True)
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

     




    class Meta:
        # swappable = 'AUTH_USER_MODEL'
        ordering = ['-date']


    def __str__(self):
        if self.full_name:
            return f"{self.user.uid} - {self.user.full_name}"
        else:
            return f"{self.user.uid} - {self.user.username}"
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender= User)
post_save.connect(save_user_profile, sender= User)
