from django.contrib import admin
from .models import complaint, fault
# Register your models here.

admin.site.register(complaint)
admin.site.register(fault)