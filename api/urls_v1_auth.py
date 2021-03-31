from django.urls import path

from api.views import get_confirmation_code, get_token

urlpatterns = [
    path('auth/email/', get_confirmation_code),
    path('auth/token/', get_token),
]
