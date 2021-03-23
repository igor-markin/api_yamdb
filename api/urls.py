from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from . import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'auth', views.AuthViewSet, basename='auth')
router_v1.register(r'users', views.UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
