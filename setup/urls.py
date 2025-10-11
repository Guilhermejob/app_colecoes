from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/app_collection/', include('app_collection.urls')),
    path('api/clients/', include('client.urls')),

]
