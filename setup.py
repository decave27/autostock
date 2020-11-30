from os import environ
from setuptools import setup, find_packages
from stock import __version__ as version
import re
import os

with open("autostock/__init__.py", encoding="UTF8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)
path = = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
with open(f"{path}/requirements.txt", encoding="UTF8") as f:
    requirements = f.read().splitlines()

with open(f"README.md", encoding="UTF8") as f:
    readme = f.read()
setup(
    name = 'autostock',
    version = version,
    license = 'MIT',
    author = 'decave27',
    author_email = 'decave27@gmail.com',
    description = 'Making stock functions easy',
    long_description = readme,
    long_description_content_type = 'text/markdown',
    url = 'hhttps://github.com/decave27/autostock',
    packages = find_packages(),
    install_requires = open('requirements.txt').readlines(),
    python_requires = '>=3.6'
)
