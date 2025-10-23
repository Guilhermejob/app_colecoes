from django.urls import path
from client.views.client_view_set import ClientApiView

urlpatterns = [
    path('', ClientApiView.as_view()),         # GET (todos) / POST (criar)
    path('<int:id>/', ClientApiView.as_view()) # GET, PATCH, DELETE (por ID)
]