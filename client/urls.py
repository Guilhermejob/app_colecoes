from django.urls import path
from client.views.client_view_set import ClientApiView
from client.views.auth_views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('', ClientApiView.as_view()),         # GET (todos)
    path('<int:id>/', ClientApiView.as_view()), # GET, PATCH, DELETE (por ID)
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]