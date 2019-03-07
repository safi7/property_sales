# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in property_sales/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('property_sales/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='property_sales',
	version=version,
	description='Module related to property Sales for Setia Awan Holdings Sdn Bhd',
	author='Tektician Sdn Bhd',
	author_email='info@tektician.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
