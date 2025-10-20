from django.urls import path
from diecasts.views.Diecast_Model import DiecastModelViewSet
from diecasts.views.diecast_brand import DiecastBrandViewSet
from diecasts.views.Car_Brand import CarBrandViewSet
from diecasts.views.diecast import DiecastApiView, DiecastDetailApiView
from diecasts.views.car_model import CarModelViewSet 


urlpatterns = [
    path('', DiecastApiView.as_view()),
    path('<int:id>/',DiecastDetailApiView.as_view()),
    path('model/', DiecastModelViewSet.as_view()),
    path('brand/', DiecastBrandViewSet.as_view()),
    path('car_model/', CarModelViewSet.as_view()),
    path('car_brand/', CarBrandViewSet.as_view()),  
]
