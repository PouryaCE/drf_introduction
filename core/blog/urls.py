from rest_framework import routers
from .views import PostViewSet
from django.urls import path

app_name = 'blog'


urlpatterns = []


router = routers.SimpleRouter()
router.register(r'post', PostViewSet, basename="post")
urlpatterns = router.urls