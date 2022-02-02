import random
import string
import uuid

from django.conf import settings
from django.http import HttpRequest

from .models import GitHubScopes
from .settings import GITHUB_AUTH_SCOPE


def get_random_string(length: int = 12):
    code = str(uuid.uuid4().hex)[:length]
    return code


def id_generator(
    size: int = 8,
    chars: str = string.ascii_uppercase + string.digits
        ) -> str:
    return ''.join(random.choice(chars) for _ in range(size))


def save_state_to_db(ip: str, state: str):
    """
        Save the state to db
    """
    scope = GitHubScopes.objects.create(
        scope=state,
        ip=ip,
    )
    scope.save()
    return None


def get_github_authorization_url(request: HttpRequest, redirect_uri: str):
    """
        URL to redirect the client to
        in order to authorize from the github
    """
    github_base_url = "https://github.com/login/oauth/authorize"
    state = get_random_string(length=20)
    GITHUB_AUTH_KEY = getattr(settings, "GITHUB_AUTH_KEY", None)

    authorization_uri = "%s?client_id=%s&redirect_uri=%s&state=%s&response_type=%s&scope=%s" % (
        github_base_url,
        GITHUB_AUTH_KEY,
        redirect_uri,
        state,
        "code",
        ",".join(GITHUB_AUTH_SCOPE),
    )

    save_state_to_db(
        ip=request.META.get("REMOTE_ADDR"),
        state=state,
    )

    return authorization_uri
