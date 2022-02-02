from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

AUTH_PROVIDER = {"github": "github"}


class GitHubAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.CharField(
        choices=AUTH_PROVIDER.items(),
        default=AUTH_PROVIDER.get("github"),
        verbose_name=_("provider"),
        max_length=30,
    )
    last_login = models.DateTimeField(
        verbose_name=_("last login"),
        auto_now=True
        )
    date_joined = models.DateTimeField(
        verbose_name=_("date joined"),
        auto_now_add=True
        )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _("GitHub Account")
        verbose_name_plural = _("GitHub Accounts")


class GitHubScopes(models.Model):
    scope = models.CharField(max_length=255, unique=True)
    ip = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Github Scopes"

    def __str__(self):
        return self.scope
