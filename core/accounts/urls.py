from django.urls import path
from . import views

app_name = "accounts"


urlpatterns = [
    path("register", views.UserRegistraion.as_view(), name="register")
]