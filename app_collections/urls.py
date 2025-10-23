from django.urls import path
from app_collections.views.diecast_collection_view_set import DiecastCollectionApiView

urlpatterns = [
    path('<int:collection_id>/items/', DiecastCollectionApiView.as_view()),
    path('<int:collection_id>/items/<int:id>/', DiecastCollectionApiView.as_view()),
]