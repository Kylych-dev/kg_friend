from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed, TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from datetime import datetime


from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.account.models import CustomUser
from .serializers import UserSerializer


class UserRegisterView(APIView):
    authentication_classes = []
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class UserAuthenticateView(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny,]

    def login(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        try:
            user = CustomUser.objects.get(email=email)
            user_role = user.role
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed("Такого пользователя не существует")

        if user is None or user_role is None:
            raise AuthenticationFailed("Такого пользователя не существует")

        if not user.check_password(password):
            raise AuthenticationFailed("Не правильный пароль")

        access_token = AccessToken.for_user(user)
        refresh_token = RefreshToken.for_user(user)

        # ___________________________________________________________
        # Допольнительная ифнормация о токене
        access_token_lifetime = api_settings.ACCESS_TOKEN_LIFETIME
        refresh_token_lifetime = api_settings.REFRESH_TOKEN_LIFETIME
        current_datetime = datetime.now()
        access_token_expiration = current_datetime + access_token_lifetime
        refresh_token_expiration = current_datetime + refresh_token_lifetime
        # ___________________________________________________________

        return Response(
            data={
                "access_token": str(access_token),
                "access_token_expires": access_token_expiration.strftime("%Y-%m-%d %H:%M:%S"),

                "refresh_token": str(refresh_token),
                "refresh_token_expires": refresh_token_expiration.strftime("%Y-%m-%d %H:%M:%S"),

                "token_type": "access",
                "status": "success"
            },
            status=status.HTTP_200_OK,
        )

    def logout(self, request):
        try:
            if "refresh_token" in request.data:
                refresh_token = request.data["refresh_token"]
                if refresh_token:
                    token = RefreshToken(refresh_token)
                    token.blacklist()
                return Response("Вы вышли из учетной записи", status=status.HTTP_200_OK)
            else:
                return Response(
                    "Отсутствует refresh_token", status=status.HTTP_400_BAD_REQUEST
                )
        except TokenError:
            raise AuthenticationFailed("Не правильный токен")

