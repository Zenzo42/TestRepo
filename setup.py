import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='krules-mongodb',
    version="0.4.0",
    author="Alberto Degli Esposti",
    author_email="alberto@arispot.tech",
    description="KRules Python mongodb support package",
    licence="Apache Licence 2.0",
    keywords="krules rules mongodb ",
    url="https://github.com/airspot-dev/krules-mongodb",
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
    ],
    install_requires=[
        'pymongo==3.9.0',
        'krules-core==0.4.0'
    ],
    setup_requires=[
        'pytest-runner',

    ],
    tests_require=[
        'pytest',
    ],
)