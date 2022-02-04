django-rest-github-oauth
========================


.. image:: https://img.shields.io/pypi/v/django_rest_github_oauth.svg
        :target: https://pypi.python.org/pypi/django_rest_github_oauth

.. image:: https://img.shields.io/travis/mabdullahadeel/django-rest-github-oauth.svg
        :target: https://travis-ci.com/mabdullahadeel/django-rest-github-oauth

.. image:: https://readthedocs.org/projects/django-rest-github-oauth/badge/?version=latest
        :target: https://django-rest-github-oauth.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/mabdullahadeel/django-rest-github-oauth/shield.svg
     :target: https://pyup.io/repos/github/mabdullahadeel/django-rest-github-oauth/
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


For detailed information regarding the installation, see the `installation guide`_.

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

.. note::
    * If you are using Token Authentication, please header over to `djangorestframework token authentication`_ and add related settings to your ``settings.py``

    * If you are using JWT Authentication, please header over to `djangorestframework simple jwt`_ and add related settings to your ``settings.py``

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

    You need to set the ``GITHUB_AUTH_CALLBACK_URL`` the same value you set on **github** while creating the app.

Then add the following to you main ``urls.py`` file.

.. code-block:: python

    urlpatterns = [
      # ...
      path('admin/', admin.site.urls),
      path('auth/github/', include('django_rest_github_oauth.urls')),
      # ...
    ]

Run migrations

.. code-block:: bash

    python manage.py migrate

That's all you have to do on the backend.

Usage
######

To get ``authorizaition_uri``, make a ``GET`` request to the following url::

    http://localhost:8000/auth/github?redirect_uri=http://localhost:3000/auth/success/

This will return a payload of the form

.. code-block:: JSON

    {
        "data": {
            "authorization_uri": "https://github.com/login/oauth/authorize?client_id=shlf898f7dsfsd0f90wer9fs&redirect_uri=http://localhost:3000/auth/success/&state=dac7944888d140e19280&response_type=code&scope=user:email,read:user"
             },
        "message": "success",
        "error": false
    }

Redirect your user to ``authorization_uri``.

Then, after the user has authorized your app, they will be redirected to the ``GITHUB_AUTH_CALLBACK_URL`` you specified with two query parameters:

* ``code``
* ``state``

In your frontend javascript, read those query parameters. Here is a quick snippet how you can achieve that.

.. code-block:: javascript

    const query = new URLSearchParams(window.location.search);
    const code = query.get("code");
    const state = query.get("state");

Then make a ``POST`` request to the following url with ``code`` and ``state`` in the request body::

    http://localhost:8000/auth/github

The reuturn payload will have user informations and appropriate tokens.

Here is a snippet how you can make call using ``axios``.

.. code-block:: javascript

    const query = new URLSearchParams(window.location.search);
    const code = query.get("code");
    const state = query.get("state");

    const details = {
      code: code,
      state: state,
    };

    const url = "http://127.0.0.1:8000/auth/github/";

    axios({
      method: "post",
      url: url,
      data: details,
      })
      .then((response) => {
        console.log(response)
        // login the user and save token for further request to the backend
      })
      .catch((err) => console.log(err));

.. _djangorestframework token authentication: https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication
.. _djangorestframework simple jwt: https://www.djangorestframework.org-rest-framework-simplejwt.readthedocs.io/en/latest
.. _register app with github: https://github.com/settings/applications/new
.. _installation guide: https://django-rest-github-oauth.readthedocs.io/en/latest/installation.html
