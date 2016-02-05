#!/usr/bin/env python
from setuptools import setup

exec(open("django_google_storage/version.py").read())

setup(
    name='django_google_storage',
    version=__version__,
    description='Class Client for Google Cloud Storage.',
    author='Jonatan Rodriguez',
    author_email='jrperdomoz@gmail.com',
    maintainer='Jonatan Rodriguez',
    maintainer_email='jrperdomoz@gmail.com',
    url='https://github.com/jrperdomoz/GoogleCloudStorage',
    license="BSD",
    # packages=[''],
    # long_description=open("README.md").read(),
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Programming Language :: Python :: 2.7'
        # 'License :: OSI Approved :: Apache Software License',
        # 'Programming Language :: Python :: 2.6',
        # 'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3.3',
    ],
    install_requires=['django', 'gcloud'],
    keywords='google cloud storage django',
)
