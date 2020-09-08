import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='krules-cloudstorage',
    version="0.4.2",
    author="Alberto Degli Esposti",
    author_email="alberto@arispot.tech",
    description="KRules Python cloudstorage support package",
    licence="Apache Licence 2.0",
    keywords="krules rules engine gcp cloudstorage bucket",
    url="https://github.com/airspot-dev/krules-cloudstorage",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        'google-cloud-storage==1.20.0',
        'cloudstorage==0.10.0',
        'krules-core==0.4.2'
    ],
    setup_requires=[
        'pytest-runner',

    ],
    tests_require=[
        'pytest',
    ],
)
