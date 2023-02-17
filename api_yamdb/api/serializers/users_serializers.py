from rest_framework import serializers

from core.models.users import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name','last_name','username',
                  'email','bio','role')
        model = User

    def validate_username(self, username):
        if username == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )
        return username

    def validate_email(self, email):
        if email == "":
            raise serializers.ValidationError('Поле почты не заолненно')
        return email

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
