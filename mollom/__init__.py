"""Support for the Mollom content filtering system

This package contains the following modules:

HTTPTransport -- a class for transporting XMLRPC requests, fixing the
                 problems from the standard Transport class in the
                 Python XMLRPC library.

Mollom -- Implementation of the Mollom protocol, allowing interaction
          with the Mollom service from Python.

"""
# this is a namespace package
try:
    import pkg_resources
    pkg_resources.declare_namespace(__name__)
except ImportError:
    import pkgutil
    __path__ = pkgutil.extend_path(__path__, __name__)

from Mollom import *
