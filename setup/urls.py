from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/app_collection/', include('app_collections.urls')),
    path('api/clients/', include('client.urls')),
    path('api/diecasts/', include('diecasts.urls')),
]
