import random
from typing import Tuple

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

from .models import GitHubAccount
from .response import UserResponse
from .utils import id_generator


class RegisterSocialUser:
    @staticmethod
    def generate_username(name: str) -> str:
        username = "".join(name.split(" ")).lower()
        if not get_user_model().objects.filter(username=username).exists():
            return username
        else:
            random_username = username + str(random.randint(0, 1000))
            return RegisterSocialUser.generate_username(random_username)

    @staticmethod
    def get_names(user_data: dict) -> Tuple:
        name: str = user_data.get("name")
        names: list = name.split(" ")
        return names[0], names[1]

    def register_social_user(provider: str, user_data: dict) -> str:
        filtering_by_email = get_user_model().objects.filter(email=user_data.get("email"))

        if filtering_by_email.exists():
            user: User = filtering_by_email.first()
            user_gh_account = GitHubAccount.objects.filter(user=user)
            if user_gh_account.exists():
                return UserResponse.get_user_payload(user)
            else:
                raise AuthenticationFailed(detail='Please continue your login with github')
        else:
            username = RegisterSocialUser.generate_username(user_data.get("login") or user_data.get("name"))
            first_name, last_name = RegisterSocialUser.get_names(user_data)
            t_password: str = id_generator()
            user: User = get_user_model().objects.create_user(
                username=username,
                email=user_data.get("email"),
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(t_password)

            GitHubAccount.objects.create(user=user).save()
            user.save()
            return UserResponse.get_user_payload(user)
