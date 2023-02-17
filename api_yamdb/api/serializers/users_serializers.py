import re

from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.models.users import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField('^[\w.@+-]+$')
    email = serializers.EmailField(required=True, max_length=254)

    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        model = User

    def validate_username(self, value):
        if len(value) > settings.MAX_USERNAME_LENGTH:
            raise ValidationError("Длина username не должна быть более "
                                  f"{settings.MAX_USERNAME_LENGTH} символов")
        return value


class UserPatchSerializer(serializers.ModelSerializer):
    username = serializers.RegexField('^[\w.@+-]+$')
    email = serializers.EmailField(required=True, max_length=254)
    role = serializers.StringRelatedField(read_only=True)
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name', 'bio', 'role')
        model = User

    def validate_username(self, value):
        if len(value) > settings.MAX_USERNAME_LENGTH:
            raise ValidationError("Длина username не должна быть более "
                                  f"{settings.MAX_USERNAME_LENGTH} символов")
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email',)

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return value
