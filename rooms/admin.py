from django.contrib import admin
from .models import Room, RoomType 

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = [ 'number', 'hostel',]
    prepopulated_fields = {'slug': ('number', )}

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'hostel',]
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)

