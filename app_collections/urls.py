from django.urls import path, include
from rest_framework import routers
from app_collections.views.diecast_collection_view_set import CollectionViewSet, CollectionItemViewSet



router = routers.DefaultRouter()
router.register(r'register_collection', CollectionViewSet, basename='register_collection')
router.register(r'add_diecast', CollectionItemViewSet, basename='add_diecast')


urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
