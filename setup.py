# -*- coding: utf-8 -*-
"""Package description"""
from setuptools import setup, find_packages

version = "0.1.0"

setup(name="shaura_example", version=version,
  author="Asko Soukka",
  author_email="asko.soukka@iki.fi",
  description="An example Shaura application for Google App Engine",
  long_description=open("README.rst").read() + "\n" +
                   open("HISTORY.txt").read(),
  license="GPL3",
  # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
  keywords="",
  classifiers=[
    "Programming Language :: Python",
  ],
  url="https://github.com/datakurre/shaura_example",
  packages=find_packages(exclude=["ez_setup"]),
  namespace_packages=[],
  zip_safe=False,
  install_requires=[
    "setuptools",
    # -*- Extra requirements: -*-
    "shaura[gae]",
  ],
  extras_require = {"test": ["corejet.core"]},
)
