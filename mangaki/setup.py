
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='mangaki',
    version='0.6.1',
    description='Open source website for anime and manga recommendations',
    python_requires='==3.*,>=3.7.0',
    project_urls={"homepage": "https://mangaki.fr"},
    author='Mangaki team',
    author_email='contact@mangaki.fr',
    maintainer='Ryan Lahfa',
    maintainer_email='masterancpp@gmail.com',
    license='GPL-3.0',
    packages=['irl', 'irl.migrations', 'mangaki', 'mangaki.api', 'mangaki.utils', 'mangaki.migrations',
        'mangaki.management', 'mangaki.templatetags'],
    package_dir={"": "."},
    package_data={"mangaki": ["locale/*", "static/*", "templates/*", "wrappers/*"]},
    install_requires=['beautifulsoup4', 'celery==4.*,>=4.2.0', 'coreapi==2.*,>=2.3.0', 'django==2.*,>=2.2.0', 'django-allauth==0.*,>=0.41.0', 'django-bootstrap4!=1.1.1', 'django-celery-beat==1.*,>=1.1.0', 'django-js-reverse==0.*,>=0.9.0', 'django-sendfile==0.*,>=0.3.0', 'djangorestframework==3.*,>=3.9.0', 'jinja2', 'lxml==4.*,>=4.4.0', 'mangaki-zero', 'markdown==3.*,>=3.0.0', 'natsort==7.*,>=7.0.1', 'psycopg2-binary', 'python-redis-lock==3.*,>=3.2.0', 'raven==6.*,>=6.1.0', 'redis==3.*,>=3.2.0'],
    dependency_links=['git+https://github.com/mangaki/zero@master#egg=mangaki-zero'],
)
