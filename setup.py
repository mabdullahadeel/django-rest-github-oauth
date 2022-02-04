#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "Django >= 2.0",
    "djangorestframework >= 3.0",
    "requests >= 2.0",
]

test_requirements = ['pytest>=3', ]

setup(
    author="Abdullah Adeel",
    author_email='business.info.abd@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
    ],
    description="A simple python library to authenticate users with github in Django applications.",
    entry_points={},
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['django_rest_github_oauth', 'django', 'github', 'oauth', 'rest', 'restframework'],
    name='django-rest-github-oauth',
    packages=find_packages(include=['django_rest_github_oauth', 'django_rest_github_oauth.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mabdullahadeel/django-rest-github-oauth',
    version='0.1.1',
    zip_safe=False,
)
