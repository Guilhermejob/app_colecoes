from rest_framework import routers
from django.urls import path, include
from diecasts.views.Diecast_Model import DiecastModelViewSet
from diecasts.views.diecast_brand import DiecastBrandViewSet
from diecasts.views.Car_Brand import CarBrandViewSet
from diecasts.views.diecast import DiecastViewSet
from diecasts.views.car_model import CarModelViewSet 

router = routers.DefaultRouter()
router.register(r'register_diecast', DiecastViewSet, basename='register_diecast')
router.register(r'register_diecast_model', DiecastModelViewSet, basename='register_diecast_model')
router.register(r'register_diecast_brand', DiecastBrandViewSet, basename='register_diecast_brand')
router.register(r'register_car_brand', CarBrandViewSet, basename='register_car_brand')
router.register(r'register_car_model', CarModelViewSet, basename='register_car_model')

urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
