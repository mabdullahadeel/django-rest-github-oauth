from typing import List

from django.conf import settings
from django.http import HttpRequest
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .github import GitHubAuth
from .models import GitHubScopes
from .response import APIResponse
from .settings import GITHUB_AUTH_ALLOWED_REDIRECT_URIS
from .utils import get_github_authorization_url


class GitHubLogin(APIView):
    permission_classes = (AllowAny,)

    def get(self, request: HttpRequest, *args, **kwargs):
        """
            returns an authorization_uri to
            redirect the user along with the
            state to track CSRF
        """
        redirect_uri = request.GET.get('redirect_uri', None)
        ALLOWED_REDIRECT_URIS: List[str] = getattr(
            settings,
            "GITHUB_AUTH_ALLOWED_REDIRECT_URIS",
            GITHUB_AUTH_ALLOWED_REDIRECT_URIS
        )
        if not redirect_uri or redirect_uri not in ALLOWED_REDIRECT_URIS:
            return APIResponse.error(data={"error": "Invalid redirect_uri"})

        authorization_uri = get_github_authorization_url(request=request, redirect_uri=redirect_uri)
        return APIResponse.success(data={"authorization_uri": authorization_uri})

    def post(self, request: HttpRequest, *args, **kwargs):
        try:
            state = request.data.get('state', None)
            if not state:
                return APIResponse.error(data={"error": "Invalid State"})

            matching_state = GitHubScopes.objects.filter(scope=state)
            if not matching_state:
                return APIResponse.error(
                    data={"error": "Invalid State"},
                    status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                )

            oauth_scopes: GitHubScopes = matching_state[0]
            if oauth_scopes.ip != request.META.get('REMOTE_ADDR'):
                return APIResponse.error(
                    data={"error": "Invalid IP"},
                    status_code=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                )
            else:
                oauth_scopes.delete()

            return APIResponse.success(
                data=GitHubAuth(code=request.data.get('code', None)).login_user(),
                status_code=status.HTTP_201_CREATED
                )
        except Exception as e:
            return APIResponse.error(
                data={"error": str(e)},
                )
