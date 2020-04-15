# Python Library Template

This repository contains a cookiecutter template that can be used for library development. 
Build, install and tests of the library are run by tox, the documentation is built with sphinx and a
helper script (both also invoked by tox).

In the documentation links to source code will be created, therefore you will be prompted to give the project's host url. 
It will typically be of the form `https://<host>/<postfix>`.

See the resulting project's [readme]({{cookiecutter.project_name}}/README.md) for further details