from django.contrib import admin
from hostel.models import Hostel, HostelFeatures, HostelGallery, HotelFaqs

# Register your models here.
class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'user', 'thumbnail']
    prepopulated_fields = {'slug': ('name', )}



class HostelFeaturesAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'hostel']

class HostelFAQSAdmin(admin.ModelAdmin):
    list_display = ['question']


admin.site.register(Hostel, HostelAdmin)
admin.site.register(HotelFaqs, HostelFAQSAdmin)
admin.site.register(HostelFeatures, HostelFeaturesAdmin)
admin.site.register(HostelGallery)




