#!/usr/bin/env python3
# coding: utf-8
from setuptools import setup, find_packages
import sys

setup(
    name='allfiles',
    version='1.0',
    description='iterate files in directory treesfnmatchcase',
    long_description=open('README.rst', encoding='utf-8').read(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    keywords=[''],
    author='OMOTO Kenji',
    author_email='doloopwhile@gmail.com',
    license='MIT',
    install_requires=[],
    packages=find_packages(),
    test_suite='',
    tests_require=[''],
)