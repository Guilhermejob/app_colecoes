from rest_framework import routers
from django.urls import path, include
from app_collection.views.Diecast_Model import DiecastModelViewSet
from app_collection.views.diecast_brand import DiecastBrandViewSet
from app_collection.views.Car_Brand import CarBrandViewSet
from app_collection.views.diecast import DiecastViewSet
from app_collection.views.car_model import CarModelViewSet 

router = routers.DefaultRouter()
router.register(r'diecast', DiecastViewSet, basename='diecast')
router.register(r'diecast-model', DiecastModelViewSet, basename='diecastmodel')
router.register(r'diecast-brand', DiecastBrandViewSet, basename='diecastbrand')
router.register(r'car-brand', CarBrandViewSet, basename='carbrand')
router.register(r'car-model', CarModelViewSet, basename='carmodel')

urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
