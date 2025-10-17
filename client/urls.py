from django.urls import path, include
from rest_framework import routers
from client.views.client_view_set import ClientViewSet, GetClientById


router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)


urlpatterns = [
    path('', include(router.urls)),  # todas as rotas do router
    path('/<int:id>/', GetClientById.as_view())
]
