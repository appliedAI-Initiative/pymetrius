# Pymetrius - cookiecutter for python libraries

This repository contains a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template 
that can be used for library development. The template contains several well-known "best-practices" for libraries
 (mypy, ruff, sphinx, nbsphinx, coverage, pylint etc) and also some tools 
inspired by projects of ours that we consider generally useful - build and release scripts,
auto-generation of documentation files, links for jumping directly to the correct place in the source code and others.
Earlier versions of this template were used in several industry projects as well as for open source libraries.

Build, install and tests of the library are run by default poetry tasks, the documentation is built with Jupyter-Books.
The template includes ci/cd pipelines for github actions. We make use of [github pages](https://pages.github.com/) through the
[github-pages-deploy-action](https://github.com/JamesIves/github-pages-deploy-action). You should configure the pages source to be the root directory of the branch gh-pages.

In the documentation links to source code will be created, therefore you will be prompted to give the project's url.

See the resulting repository's [developer's readme]({{cookiecutter.project_name}}/docs/04_contributing/04_contributing.rst) 
for further details. An example of the current output of this template is in [pymetrius_output](https://github.com/appliedAI-Initiative/pymetrius_output)

# Usage

## Prerequisites

The template supports python 3.11 and higher. For a smooth project generation you need to have

1) Python of the correct version installed on your system.
2) Cookiecutter. Install it e.g. with `pip install cookiecutter`


## Creating a new project

Call

```shell script
cookiecutter https://github.com/appliedAI-Initiative/python_library_template -o path/to/directory
```

and walk through the questions. You can also clone this repository, adjust the template and call cookiecutter on
the local file.

You will get a repo in `<path/to/directory>/<project_name>`, which will contain your new library installed in 
"editable mode" (i.e. with `pip install -e`, we reccomend installing in poetry with `poetry install --with dev` ). 
The virtual environment is created by poetry. Documentation is built with jupyter-book and is published on github pages.


# Contributing
The core maintainers are Michael Panchenko and Adrian Rumpold at appliedAI.
We are happy about any contribution to this project, feel free to contact us directly or to open an issue or a pull request.