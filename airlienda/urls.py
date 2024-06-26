
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from hostel.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    

    # custom Auth urls
    path('', include('core.urls')),
    path('user/', include('userauth.urls')),
    path('hostel/', include('hostel.urls')),
    path('rooms/', include(('rooms.urls', 'rooms'), namespace='rooms')),
    path('booking/', include('booking.urls', namespace='booking')),

    # ck editor
    path('ckeditor5/', include('django_ckeditor_5.urls'))

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]




urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

