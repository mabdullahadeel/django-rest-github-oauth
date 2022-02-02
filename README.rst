django-rest-github-oauth
========================


.. image:: https://img.shields.io/pypi/v/django_rest_github_oauth.svg
        :target: https://pypi.python.org/pypi/django_rest_github_oauth

.. image:: https://img.shields.io/travis/mabdullahadeel/django_rest_github_oauth.svg
        :target: https://travis-ci.com/mabdullahadeel/django_rest_github_oauth

.. image:: https://readthedocs.org/projects/django-rest-github-oauth/badge/?version=latest
        :target: https://django-rest-github-oauth.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mabdullahadeel/django_rest_github_oauth/shield.svg
     :target: https://pyup.io/repos/github/mabdullahadeel/django_rest_github_oauth/
     :alt: Updates



A simple python library to authenticate users with github in Django applications.


* Free software: MIT license
* Documentation: https://django-rest-github-oauth.readthedocs.io.


Requirements
############

* Python (3.7, 3.8, 3.9)
* Django (2.x, 3.x, 4.x)
* Django REST Framework (3.10, 3.11, 3.12)

Setup
###############

Install the package in your python environment using ``pip``.

.. code-block:: bash

        pip install django-rest-github-oauth


For detailed information regarding the installation, see the :ref:`installation guide <target to installation>`.

Then your django project must be configured to use the library. For that include it
in ``INSTALLED_APPS`` of your ``settings.py``. Besides that, you will have to include the auth handler app in installed apps.

Currently, ``django-rest-github-oauth`` supports the following authentication backends:

* Token Authentication using `djangorestframework token authentication`_
* JWT Authentication using `djangorestframework simple jwt`_

Using JWT

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'rest_framework_simplejwt',
        'django_rest_github_oauth',
        # ...
    ]


Using Token Authentication

.. code-block:: python

    INSTALLED_APPS = [
        # ...
        'rest_framework.authtoken',
        'django_rest_github_oauth',
        # ...
    ]


Then add the following to your ``settings.py``:

.. code-block:: python

    GITHUB_AUTH_KEY = "<your_github_app_key>"
    GITHUB_AUTH_SECRET = "<your_github_app_secret>"
    GITHUB_AUTH_USE_JWT = True    # False if you're using token based authentication

    GITHUB_AUTH_CALLBACK_URL = "http://localhost:3000/auth/success/"    # url of the frontend handling redirects from github
    GITHUB_AUTH_ALLOWED_REDIRECT_URIS = [
            GITHUB_AUTH_CALLBACK_URL
        ]

.. note::

    If you have not yet created an app on github, you need to create an app to
    get the client id and secret. `register app with github`_.

.. warning::

    You need to set the ``GITHUB_AUTH_CALLBACK_URL`` you set on github while creating the app.

.. _djangorestframework token authentication: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
.. _djangorestframework simple jwt: https://www.djangorestframework.org-rest-framework-simplejwt.readthedocs.io/en/latest
.. _register app with github: https://github.com/settings/applications/new
