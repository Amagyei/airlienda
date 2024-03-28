
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    

    # custom Auth urls
    path('', include('core.urls')),
    path('user/', include('userauth.urls')),
    path('hostel/', include('hostel.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
