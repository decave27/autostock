from os import environ
from setuptools import setup, find_packages
from stock import __version__ as version

setup(
    name = 'autostock',
    version = version,
    license = 'MIT',
    author = 'decave27',
    author_email = 'decave27@gmail.com',
    description = 'Making stock functions easy',
    long_description = '[github](https://github.com/decave27/autostock)',
    long_description_content_type = 'text/markdown',
    url = 'hhttps://github.com/decave27/autostock',
    packages = find_packages(),
    install_requires = open('requirements.txt').readlines(),
    python_requires = '>=3.6'
)
