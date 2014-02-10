from setuptools import setup, find_packages

"""Setup script for PyMollom"""
from distutils.core import setup

setup(name='PyMollom',
      version='0.1',
      license='GPL',
      namespace_packages=['mollom'],
      zip_safe=False,
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=False,
      description='A Python library for the Mollom anti-spam service',
      long_description=open('README.rst').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Filters',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          ],
      )
