#!c:\python27\python.exe

from os import path
from distutils.core import setup
from setuptools import setup, Extension
from distutils.sysconfig import get_python_inc

incdir = path.join(get_python_inc(plat_specific=1))

module = Extension(
    "pydasm",
    include_dirs = [incdir],
    libraries = [],
    library_dirs = [],
    sources = ['./pydbg/pydasm/libdasm/libdasm.c', './pydbg/pydasm/pydasm.c']
)

setup( name     = "pydbg",
    version     = "1.0",
    description = "pydbg - A pure-python win32 debugger interface",
    license     = "GPL",
    packages    = ["pydbg", "utils", "pida", "pgraph"],
    ext_modules = [module]
)