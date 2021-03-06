import os
from setuptools import setup
from sprinklers import __version__

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-sprinklers",
    version = __version__,
    author = "Chris Clark",
    author_email = "chris@untrod.com",
    description = ("A simple framework for bulletproof distributed tasks with Django and Celery."),
    license = "MIT",
    keywords = "django celery sprinklers sprinkler distributed tasks",
    url = "https://github.com/chrisclark/django-sprinklers",
    packages=['sprinklers'],
    long_description=read('README.md'),
    classifiers=[
        "Topic :: Utilities",
    ],
    install_requires=[
        'Django>=1.6.7',
    ],
    include_package_data=True,
    zip_safe = False,
)
