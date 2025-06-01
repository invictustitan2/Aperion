# Stubs for distutils.command.bdist_msi

import sys
from distutils.cmd import Command

if sys.version_info >= (3,):
    class build_py(Command): ...
    class build_py_2to3(Command): ...
