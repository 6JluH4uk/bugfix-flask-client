#!/usr/bin/env python

from setuptools import setup

github_url = 'https://github.com/6JluH4uk/bugfix-flask-client.git'

setup(
    name='bugfix-flask-client',
    version = '0.0.1',
    description = 'Bugfix-flask-client',
    long_description = open('README.md', 'r').read(),
    author = 'blinchik',
    author_email = 'prohorenko_gena_@mail.ru',
    download_url = 'https://github.com/6JluH4uk/bugfix-flask-client/archive/master.zip',
    url = github_url,
    include_package_data = True,
    packages=[ 'bugfix', ],
    license = 'MIT License',
    zip_safe = False,
    install_requires = [ 'Flask', 'Flask-Admin', 'Flask-sqlalchemy'],
)
