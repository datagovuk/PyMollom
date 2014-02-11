from setuptools import setup, find_packages

"""Setup script for mollom"""
from distutils.core import setup

setup(name='mollom',
      version='0.1',
      license='GPL',
      namespace_packages=['mollom'],
      zip_safe=False,
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=False,
      description='A Python library for the Mollom anti-spam service using the original PyMollom code',
      long_description=open('README.md').read(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Filters',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          ],
      )
