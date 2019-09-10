#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

import setuptools

NAME = "ntp_pool_score"
DESCRIPTION = "Retrieve the NTP pool score for a server"
URL = "https://www.github.com/rmcintosh/ntp_pool_score"
EMAIL = "richiemcintosh@gmail.com"
AUTHOR = "Richie McIntosh"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "0.1"
LICENSE = "MIT"
REQUIRES = [
    "beautifulsoup4>=4.8.0",
    "bs4>=0.0.1",
    "certifi>=2019.6.16",
    "chardet>=3.0.4",
    "idna>=2.8",
    "requests>=2.22.0",
    "soupsieve>=1.9.3",
    "urllib3>=1.25.3"
]
TESTS_REQUIRE = ["nose"]

here = os.path.abspath(os.path.dirname(__file__))


try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    packages=setuptools.find_packages(exclude=["tests"]),
    zip_safe=False,
    install_requires=REQUIRES,
    python_requires=REQUIRES_PYTHON,
    tests_require=TESTS_REQUIRE
)
