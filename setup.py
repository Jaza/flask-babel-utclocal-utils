import os

import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'flask_babel_utclocal_utils.py')
version_line = [line for line in open(module_path)
                if line.startswith('__version__')][0]

__version__ = version_line.split('__version__ = ')[-1][1:][:-2]

setuptools.setup(
    name="flask-babel-utclocal-utils",
    version=__version__,
    url="https://github.com/Jaza/flask-babel-utclocal-utils",

    author="Jeremy Epstein",
    author_email="jazepstein@gmail.com",

    description="UTC to local (and vice versa) datetime conversion utilities for use with Flask-Babel.",
    long_description=open('README.rst').read(),

    py_modules=['flask_babel_utclocal_utils'],
    zip_safe=False,
    platforms='any',

    install_requires=['Flask', 'Flask-Babel'],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
