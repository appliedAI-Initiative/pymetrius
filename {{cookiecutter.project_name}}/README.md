# {{cookiecutter.project_name}}

This repository contains a library template with utilities for building, testing, documentation 
and configuration management.

## Workflow
Automated builds, tests, generation of docu and publishing should be handled by cicd pipelines. 
You might already have an initial version of the pipeline here. Below you will find further details on testing 
and documentation. 

Before pushing your changes to the remote it is often useful to execute `tox` locally in order to
detect mistakes early on.

We strongly suggest to use some form of virtual environment for working with the library. E.g. with conda:
```shell script
conda create -n {{cookiecutter.project_name}} python={{cookiecutter.python_version}}
conda activate {{cookiecutter.project_name}}
pip install -r requirements.txt
```

### Testing and packaging
The library is tested with tox which will build and install the package and run pytest and doctest. 
You can run it locally by installing tox into you virtual environment 
(e.g. with `pip install tox`) and executing `tox`. 

For creating a package locally run
```shell script
python setup.py sdist bdist_wheel
```

### Documentation
Documentation is built with sphinx every time tox is executed. 
There is a helper script for updating documentation files automatically. It is called by tox on built and can 
also be invoked as
```bash
python scripts/update_docs.py
```
See the code documentation in the script for more details on that

## Configuration
The repository also includes configuration utilities that are often useful when using data-related libraries. 
They do not form part of the resulting package, you can (and probably should) adjust them to your needs.

## CI/CD
Depending on the provider you chose for CICD, this repo might already contain a rudimentary CI/CD pipeline. 
The pipelines serve for building and testing the library and for publishing the resulting package and documentation.
You will probably have to further adjust it to your needs.

### Note
You might wonder why the requirements.txt already contains numpy. The reason is that tox seems to have a problem with empty
requirements files. Feel free to remove numpy once you have non-trivial requirements