# Python Library Template

This repository contains a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template 
that can be used for library development. The template contains several well-known "best-practices" for libraries
 (tox, sphinx, nbsphinx, coverage, pylint etc) and also some tools 
inspired by past projects of mine that I consider generally useful - configuration helpers, 
auto-generation of documentation files, links for jumping directly to the correct place in the source code and others.

Build, install and tests of the library are run by tox, the documentation is built with sphinx and a
helper script (both also invoked by tox). The resulting repository will contain a gitlab ci/cd pipeline that will 
run the test suite and publish docu, badges and reports.

In the documentation links to source code will be created, therefore you will be prompted to give the project's 
path relative to our gitlab url (https://gitlab.aai.lab/).

See the resulting repository's [readme]({{cookiecutter.project_name}}/README-dev.md) for further details

# Usage

## Prerequisites

The template supports python 3.8 and higher. For a smooth project generation you need to have

1) Python of the correct version installed on your system.
2) The venv module for that python version. If not installed yet, you can install it with
    ```shell script
    sudo apt-get update && apt-get install python<VERSION>-venv
    ```
3) Cookiecutter. Install it e.g. with `pip install cookiecutter`
4) You should set up a new gitlab repo in https://gitlab.aai.lab/<gitlab_project_path>. Add your credentials,
create the develop branch and mark it as default branch. This can also be done after the project
was generated locally.


## Creating a new project

Call

```shell script
cookiecutter https://gitlab.aai.lab/resources/python_library_template -o path/to/directory
```

and walk through the questions. You can also clone this repository, adjust the template and call cookiecutter on
the local file.

You will get a repo in `<path/to/directory>/<project_name>` with a venv inside it; the venv will contain your new
library in an "editable mode".
If you prefer to use a different virtual environment (like conda), feel free to delete the venv. 

The repo will be connected to the remote gitlab_project_path https://gitlab.aai.lab/<gitlab_project_path>.
After the project is generated, and the gitlab repo was set up, 
mark the develop branch as default, and simply call `git push`


# Contributing
At the moment this template is maintained only by Michael Panchenko.
I am happy about any contribution to this project, feel free to contact me directly or to open an issue or a pull request.