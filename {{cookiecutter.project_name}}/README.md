# {{cookiecutter.project_name}}

This repository contains a library template with utilities for building, testing, 
documentation and configuration management.

## Testing and packaging
The library is tested with tox which will build and install the package and run pytest and doctest. 
You can run it locally by installing tox into you virtual environment 
(e.g. with `pip install tox`) and executing `tox`. 

For creating a package locally run
```shell script
python setup.py sdist bdist_wheel
```

## Documentation
Documentation is built with sphinx every time tox is executed. 
There is a helper script for updating documentation files automatically, it can be invoked as
```bash
python scripts/update_docs.py
```
See the code documentation in the script for more details on that

## Configuration
The repository also includes configuration utilities that are often useful when using data-related libraries. 
They do not form part of the resulting package, you can (and probably should) adjust them to your needs.

## CI/CD
The repo contains rudimentary CI/CD pipelines for multiple providers (gitlab, github, azure dev-ops, readthedocs and others). 
The pipelines serve for building and testing the library and for publishing the resulting package and documentation.
Delete the ones you don't need and adjust the rest to your needs.

### Note
You might wonder why the requirements.txt already contains numpy. The reason is that tox seems to have a problem with empty
requirements files. Feel free to remove numpy once you have non-trivial requirements