from django.urls import path, include
from rest_framework import routers
from client.views.diecast_collection_view_set import DiecastCollectionsViewSet
from client.views.client_view_set import ClientViewSet


router = routers.DefaultRouter()
router.register(r'collections', DiecastCollectionsViewSet, basename='collections')
router.register(r'clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
