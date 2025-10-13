from django.urls import path, include
from rest_framework import routers
from client.views.diecast_collection_view_set import CollectionViewSet, CollectionItemViewSet
from client.views.client_view_set import ClientViewSet


router = routers.DefaultRouter()
router.register(r'collections', CollectionViewSet, basename='collections')
router.register(r'register_client', ClientViewSet, basename='clients')
router.register(r'add_diecast', CollectionItemViewSet, basename='collection-items')


urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
