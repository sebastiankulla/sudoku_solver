#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = []
test_requirements = []

setup(
    author="Sebastian Kulla",
    author_email='sebastiankulla90@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A small tool that allows solving Soduko via backtracking algorithm.",
    install_requires=requirements,
    license="MIT license",
    include_package_data=True,
    keywords='sudoku_solver',
    name='sudoku_solver',
    packages=find_packages(include=['sudoku_solver', 'sudoku_solver.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/sebastiankulla/sudoku_solver',
    version='0.1.0',
    zip_safe=False,
)
