#!/usr/bin/env python
from setuptools import setup


setup(
    name='django-ldap-server',
    description='share django users and groups with other services via ldap',
    version='0.1.0',
    author='Lars Kreisz & Martin Mrose',
    author_email='der.kraiz@gmail.com',
    license='MIT',
    url='https://github.com/ponyriders/django-ldap-server',
    packages=['django_ldap_server'],
    long_description=open('README.rst').read(),
    install_requires = [
        'gevent==dev',
        'django>=1.4',
        'pyasn1-modules==0.0.5'
    ],
    dependency_links= [
        'https://github.com/surfly/gevent/tarball/master#egg=gevent'
    ]
)