from rest_framework import serializers

from .models import Category, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')
        read_only_fields = ('role', 'email')


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ['id', ]
        model = Category
