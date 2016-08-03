import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="django-rql-filter",
    version="0.0.0",
    author="Nicolas Joyard",
    author_email="joyard.nicolas@gmail.com",
    description=("A RQL-enabled filter backend for django-rest-framework"),
    license="MIT",
    keywords="django filter drf rest rql rsql fiql",
    url="https://github.com/njoyard/django-rql-filter",
    packages=['rql_filter'],
    long_description=read('README.md'),
    install_requires=[
        'grako>=3,<4',
    ],
    extras_require={
        'testing': [
            'djangorestframework>=3,<4',
            'flake8>=2,<3',
            'pytest>=2,<3',
            'pytest-django>=2,<3',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
    ],
)
