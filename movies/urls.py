# In your app's urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)  # Register your viewset here

urlpatterns = [
    path('', include(router.urls)),
]
