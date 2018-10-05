# pydbg

A pure-python win32 debugger interface. This release includes the missing dependencies and [pydasm](https://github.com/axcheron/pydasm), a python wrapper for [libdasm](https://github.com/axcheron/libdasm).

## Installation

First, install [Microsoft Visual C++ Compiler for Python 2.7](https://www.microsoft.com/en-us/download/details.aspx?id=44266).

Then, clone the repository with the submodules :

```bash
git clone --recurse-submodules https://github.com/axcheron/pydbg.git
python setup.py install
```

Also, if you don't already have it, you can find the last version of [Python 2.7 here](https://www.python.org/downloads/).

## License

This project is released under the GNU license. See LICENCE.