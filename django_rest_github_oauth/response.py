from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response


class APIResponse:
    @staticmethod
    def success(data=[], message="success", status_code=status.HTTP_200_OK) -> Response:
        return Response(
            {
                "data": data,
                "message": message,
                "error": False,
            },
            status=status_code
        )

    @staticmethod
    def error(data=[], message="Something went wrong", status_code=status.HTTP_400_BAD_REQUEST) -> Response:
        return Response(
            {
                "data": data,
                "message": message,
                "error": True,
            },
            status=status_code
        )


class UserResponse:
    @staticmethod
    def generate_token(user: User):
        INSTALLED_APPS = getattr(settings, 'INSTALLED_APPS', None)
        if 'rest_framework.authtoken' not in INSTALLED_APPS:
            raise Exception("You need to add 'rest_framework.authtoken' to your INSTALLED_APPS")

        from rest_framework.authtoken.models import Token
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}

    @staticmethod
    def generate_jwt_token(user: User):
        try:
            from rest_framework_simplejwt.tokens import RefreshToken
        except ImportError:
            raise ImportError("rest_framework_simplejwt needs to be installed")
        token = RefreshToken.for_user(user)
        return {
            'tokens': {
                'access': str(token.access_token),
                'refresh': str(token)
            }
        }

    @staticmethod
    def get_auth_token(user: User):
        GITHUB_AUTH_USE_JWT = getattr(settings, "GITHUB_AUTH_USE_JWT", False)
        if GITHUB_AUTH_USE_JWT:
            return UserResponse.generate_jwt_token(user)
        return UserResponse.generate_token(user)

    @staticmethod
    def get_user_payload(user: User):
        return {
            "username": user.username,
            "email": user.email,
            "id": user.id,
            **UserResponse.get_auth_token(user)
        }
