#!/usr/bin/env python

from setuptools import setup

github_url = 'https://github.com/6JluH4uk/bugfix-client.git'
long_desc = '''
This is bugfix-client for django project's.
VERSION 0.0.1
'''

setup(
    name='bugfix-client',
    py_modules = ['bugfix'],
    version = '0.0.1',
    description = 'Bugfix-client',
    long_description = long_desc,
    author = 'blinchik',
    author_email = 'prohorenko_gena_@mail.ru',
    download_url = 'https://github.com/6JluH4uk/bugfix-client/archive/master.zip',
    url = github_url,
    include_package_data = True,
    license = 'MIT License',
    zip_safe = False,
    install_requires = [
        '',
    ],
)
