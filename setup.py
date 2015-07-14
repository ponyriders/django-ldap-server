#!/usr/bin/env python
from setuptools import setup


def get_requirements(requirements_file):
    """
    Returns a list of package requirements read from the given file.
    :param requirements_file: the file to read
    :return: list of package requirements
    """
    with open(requirements_file, 'r') as f:
        return [line for line in f.read().splitlines() if not line.startswith('#')]


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
    install_requires = get_requirements('requirements.txt'),
    tests_require=get_requirements('requirements_test.txt'),
)
