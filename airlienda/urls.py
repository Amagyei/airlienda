
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    

    # custom Auth urls
    path('', include('core.urls')),
    path('user/', include('userauth.urls')),
]
