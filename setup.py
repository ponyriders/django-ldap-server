#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-ldap-server',
    description='share django users and groups with other services via ldap',
    version='0.1.0',
    author='Lars Kreisz & Martin Mrose',
    author_email='django-ldap-server@penthranet.de',
    license='MIT',
    url='https://github.com/ponyriders/django-ldap-server',
    packages=['django_ldap_server'],
    long_description=open('README.rst').read(),
    install_requires = [
        'gevent>=1.1a1',
        'django>=1.8',
        'pyasn1-modules>=0.1.8'
    ],
)
