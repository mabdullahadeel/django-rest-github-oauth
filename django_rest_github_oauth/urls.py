from django.urls import path

from .views import GitHubLogin

urlpatterns = [
    path("github/", view=GitHubLogin.as_view(), name="github_login"),
]
