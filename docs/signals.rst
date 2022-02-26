Signals
========


``django-rest-github-oauth`` provides the following signals:

``github_user_created``
-----------------------
    Sent when a new GitHub user is created. The signal is sent with the
    newly created user instance as one of the keywords arguments.
    The user is instance of default User model specified in ``settings.py``.

    .. code-block:: python

        from django.contrib.auth.models import User
        from django.dispatch import receiver
        from rest_github_oauth.signals import github_user_created

        @receiver(github_user_created)
        def my_callback(sender, **kwargs):
            user: User = kwargs['user']
            # do something with the user
            # ...
