from django.contrib import admin

from .models import GitHubAccount, GitHubScopes

admin.site.register(GitHubScopes)
admin.site.register(GitHubAccount)
