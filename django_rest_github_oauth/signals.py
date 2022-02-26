from django.dispatch import Signal

github_user_created = Signal(providing_args=["user"])
