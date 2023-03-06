from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_views
app_name = "accounts"


urlpatterns = [
    path("register", views.UserRegistraion.as_view(), name="register"),
    path("api-token-auth/", auth_views.obtain_auth_token)
]