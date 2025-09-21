from rest_framework import routers
from django.urls import path, include
from collection.views import BrandViewSet, DiecastModelViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'diecast-model', DiecastModelViewSet, basename='diecastmodel')

urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
]
