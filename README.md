# Python Library Template

This repository contains a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template 
that can be used for library development. The template 
contains several well-known "best-practices" for libraries (tox, sphinx, coverage, pylint etc) and also some tools 
inspired by past projects of mine that I consider generally useful - configuration helpers, 
auto-generation of documentation files, links for jumping directly to the correct place in the source code and others.

Build, install and tests of the library are run by tox, the documentation is built with sphinx and a
helper script (both also invoked by tox).

The resulting repository will contain a gitlab ci/cd pipeline that will run the test suite and
publish docu, badges and reports. Badges can accessed from the pipeline's artifacts, e.g. for the coverage badge
the url will be:
```
https://gitlab.aai.lab/%{project_path}/-/jobs/artifacts/develop/raw/badges/coverage.svg?job=tox
```

In the documentation links to source code will be created, therefore you will be prompted to give the project's 
path relative to our the gitlab url (https://gitlab.aai.lab/).

See the resulting repository's [readme]({{cookiecutter.project_name}}/README.md) for further details

# Contributing
At the moment this template is maintained only by Michael Panchenko.
I am happy about any contribution to this project, feel free to contact me directly or to open an issue or a pull request.