#!/usr/bin/env python
from setuptools import setup, find_packages

from iCash import VERSION


setup(
    name='django-oscar-icash',
    version=VERSION,
    # url='https://github.com/django-oscar/django-oscar-paypal',
    description=(
        "Integration with iCash payments for django-oscar "),
    long_description=open('README.rst').read(),
    keywords="Payment, iCash, Oscar",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    install_requires=[
        'requests>=1.0'],
    extras_require={
        'oscar': ["django-oscar>=1.0"]
    },
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',        
        'Topic :: Other/Nonlisted Topic'],
)
