from django.urls import path

from .views import GitHubLogin

urlpatterns = [
    path("", view=GitHubLogin.as_view(), name="github_login"),
]
