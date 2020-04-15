# Python Library Template

This repository contains a cookiecutter template that can be used for library development. The template 
contains several well-known "best-practices" for libraries (tox, sphinx, etc) and also some tools inspired by 
past projects of mine that I consider generally useful - configuration helpers, auto-generation of documentation files, 
links for jumping directly to the correct place in the source code and so on.

Build, install and tests of the library are run by tox, the documentation is built with sphinx and a
helper script (both also invoked by tox).

In the documentation links to source code will be created, therefore you will be prompted to give the project's host url. 
It will typically be of the form `https://<host>/<postfix>`.

See the resulting repository's [readme]({{cookiecutter.project_name}}/README.md) for further details

# Contributing
At the moment this template is maintained only by Michael Panchenko.
I am happy about any contribution to this project, feel free to contact me directly or to open an issue or a pull request.