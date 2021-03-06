"""
CAUTION! Keep everything here at at minimum. Do not import stuff.
This module is imported in setup.py, so you cannot for instance
import a dependency.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from .utils.version import get_version

#: This may not be the exact version as it's subject to modification with
#: get_version() - use ``kolibri.__version__`` for the exact version string.
VERSION = (0, 10, 0, 'alpha', 0)

__author__ = 'Learning Equality'
__email__ = 'info@learningequality.org'
__version__ = str(get_version(VERSION))
