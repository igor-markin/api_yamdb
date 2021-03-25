from django.utils.crypto import get_random_string
from rest_framework import decorators, status
from rest_framework import viewsets, views, filters, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import User
from .permissions import (IsAdminOrAccessDenied, IsAdminOrReadOnly)
from .serializers import AdminUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = (IsAdminOrAccessDenied,)
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=username',)
    pagination_class = PageNumberPagination

    @action(methods=('get', 'patch'), detail=False,
            permission_classes=(permissions.IsAuthenticated,))
    def me(self, request):
        user = get_object_or_404(User, email=self.request.user.email)
        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
