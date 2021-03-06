#!/usr/bin/env python
#
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the GPLv2 license found in the LICENSE
# file in the root directory of this source tree.
#

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os
from setuptools import setup

__version__ = '0.0.1'

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='dcrpm',
    version=__version__,
    packages=['dcrpm'],
    author='Sean Karlage',
    author_email='skarlage@fb.com',
    url='https://github.com/facebookincubator/dcrpm',
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords=['dcrpm', 'rpm', 'yum', 'db_recover', 'db4', 'bdb'],
    description='A tool to detect and correct common issues around RPM database corruption.',
    long_description=long_description,
    license='GPLv2',
    install_requires=[
      'psutil',
    ],
    entry_points={
      'console_scripts': [
        'dcrpm=dcrpm.main:main',
      ],
    },
)
