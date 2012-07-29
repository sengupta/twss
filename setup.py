#!/usr/bin/env python
from distutils.core import setup

setup(
	name='twss',
	version='0.0.0',
	packages= ['twss'],
	package_data = { 'twss' : ['data/*.txt'] },
	classifiers = [
		'Operating System :: OS Independent',
	],
)

