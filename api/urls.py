from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, GenreViewSet, TitleViewSet, UserViewSet,
                    get_confirmation_code, get_token)

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)

urlpatterns = [
    path('v1/auth/email/', get_confirmation_code),
    path('v1/auth/token/', get_token),
    path('v1/', include(router_v1.urls)),
]
