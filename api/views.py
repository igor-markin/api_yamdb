
from django.utils.crypto import get_random_string
from rest_framework import decorators, status
from rest_framework import viewsets, views, filters, permissions
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import User, Review, Comment
from .permissions import (IsAdminOrAccessDenied, IsAdminOrReadOnly,
                          IsAuthorOrModeratorOrReadOnly)
from .serializers import (AdminUserSerializer, UserSerializer,
                          ReviewSerializer, CommentSerializer)


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


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthorOrModeratorOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', ]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrModeratorOrReadOnly,)
    filter_backends = [DjangoFilterBackend]


    def list(self, request, reviws_id=None):
        serializer = self.serializer_class(
            self.queryset.filter(review_id=post_id),
            many=True
        )
        return Response(serializer.data, status=status.HTTP_200_OK)