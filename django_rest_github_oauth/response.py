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
    def get_user_payload(user: User):
        return {
            "username": user.username,
            "email": user.email,
            "id": user.id,
            # "token": user.get_tokens()
        }
