#!/usr/bin/env python

from distutils.core import setup
readme = open('README.md').read()

setup(
    name='automain',
    version='1.1',
    description='A neat replacement of "if __name__ == \"main\":"',
    long_description=readme,
    author='Gerald Kaszuba',
    author_email='automain@gakman.com',
    packages=['automain'],
    )

