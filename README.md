# Python Library Template

## WORK IN PROGRESS

This repository contains a cookiecutter template that can be used for library development. 
Build, install and tests of the library are run by docs, the documentation is built with sphinx (but also through tox).


There is a helper script for updating documentation files automatically, it can be invoked as
```bash
python scripts/update_docs.py
```
See the documentation in the script for more details on that

The template also includes configuration utilities that are often useful when using data-related libraries. 
They do not form part of the resulting package, you can (and probably should) adjust them to your needs.

### Note
You might wonder why the requirements.txt already contains numpy. The reason is that tox seems to have a problem with empty
requirements files. Feel free to remove numpy once you have non-trivial requirements