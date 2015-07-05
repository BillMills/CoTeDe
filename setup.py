# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
#from distutils.core import setup

import os
import sys


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

install_requires = [
    'numpy>=1.1',
    'seabird>=0.5.8',
    'scipy',
    ]

version = '0.13.0'

setup(
    name='cotede',
    version=version,
    author='Guilherme Castelão',
    author_email='guilherme@castelao.net',
    packages=['cotede', 'cotede.qctests', 'cotede.utils', 'cotede.humanqc'],
    url='http://cotede.castelao.net',
    license='License :: OSI Approved :: BSD License',
    description='Quality Control of Temperature and Salinity profiles',
    long_description=open('README.rst').read() + '\n\n' + history,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        ],
    keywords='CTD SeaBird QualityControl oceanography hydrography',
    #package_dir = {'': './'},
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    scripts=["bin/ctdqc"],
)
