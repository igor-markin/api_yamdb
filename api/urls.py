from django.urls import include, path
from rest_framework import routers
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

<<<<<<< HEAD
from .views import UserViewSet, ReviewViewSet, CommentViewSet
=======
from .views import CategoryViewSet, GenreViewSet, TitleViewSet, UserViewSet
>>>>>>> master

router_v1 = routers.DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register(
<<<<<<< HEAD
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
=======
    'categories', CategoryViewSet, basename='categories_api'
)
router_v1.register(
    'genres', GenreViewSet, basename='genres_api'
)
router_v1.register(
    'titles', TitleViewSet, basename='titles_api'
>>>>>>> master
)


urlpatterns = [
    path('v1/', include('drfpasswordless.urls')),
    path('v1/', include(router_v1.urls)),
    path('v1/auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
