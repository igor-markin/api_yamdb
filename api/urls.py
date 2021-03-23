from django.urls import path, include
from rest_framework import routers

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'auth', views.AuthViewSet, basename='auth')
router_v1.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
