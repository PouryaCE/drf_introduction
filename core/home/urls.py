from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('questions/', views.QuestionView.as_view(), name='questions'),
    path('questions/<int:pk>/', views.QuestionView.as_view(), name='questions'),
    path('users/', views.UserShowView.as_view(), name="users"),
    path('users/create/', views.UserCreationView.as_view(), name="user-creation"),
    path('users/update/<int:pk>/', views.UserUpdateView.as_view(), name="user-update"),
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name="user-delete")
]
