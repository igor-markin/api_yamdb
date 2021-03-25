from rest_framework import serializers
from .models import User, Review, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')
        read_only_fields = ('role', 'email')


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    text = serializers.CharField()

    class Meta:
        fields = ('__all__')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    text = serializers.CharField()

    class Meta:
        fields = ('__all__')
        model = Comment