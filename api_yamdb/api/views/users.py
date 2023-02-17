from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken

from api.permissions import IsAdmin
from api.serializers.users_serializers import (
    UserSerializer, TokenSerializer, SignupSerializer)
from core.models.users import User
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdmin,)
    lookup_field = 'username'
    filter_backends = (SearchFilter,)
    search_fields = ('username')

    @action(
        methods=['GET', 'PATCH'],
        detail=False,
        permission_classes=(IsAuthenticated,),
        serializer_class=UserSerializer,
    )
    def profile(self, request):
        if request.method == "GET":
            serializer = UserSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        serializer = UserSerializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetConfirmationCodeView(GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = TokenSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data['username']
            email = serializer.data['email']
            user = get_object_or_404(User, username=username, email=email)
            send_confirmation_code(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetTokenView(GenericAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        username = serializer.data['username']
        user = get_object_or_404(User, username=username)
        confirmation_code = serializer.data['confirmation_code']
        if not default_token_generator.check_token(user, confirmation_code):
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        new_token = RefreshToken.for_user(user)
        return Response(
            {'token': str(new_token.access_token)}, status=status.HTTP_200_OK
        )


class SignUpView(GenericAPIView):
    serializer_class = SignupSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_confirmation_code(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_confirmation_code(user: User) -> int:
    confirmation_code = default_token_generator.make_token(user)
    subject = f'Код подтверждения YaMDb {confirmation_code}'
    message = f'{confirmation_code} - ваш код для авторизации на YaMDb'
    admin_email = 'example@email.com'
    user_email = [user.email]
    return send_mail(subject, message, admin_email, user_email)
