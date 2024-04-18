# Pymetrius - cookiecutter for python libraries

This repository contains a [cookiecutter](https://github.com/cookiecutter/cookiecutter) template 
that can be used for library development. The template contains several well-known "best-practices" for libraries
 (poetry, poethepoet, mypy, ruff, nbqa) and also some tools 
inspired by projects of ours that we consider generally useful - build and release scripts,
auto-generation of documentation files, and others.
Earlier versions of this template were used in several industry projects as well as for open source libraries.

Build, install and tests of the library are run by default [poethepoet](https://github.com/nat-n/poethepoet) tasks, the documentation is built with Jupyter-Book.
The template includes CI/CD pipelines based on github actions. The documentation will be published to GitHub pages using an action.

In the documentation links to source code will be created, therefore you will be prompted to give the project's url.

See the resulting repository's [contributing guidelines]({{cookiecutter.project_name}}/docs/04_contributing/04_contributing.rst) 
for further details. Some examples for projects following the general style of the template are [tianshou](https://github.com/thu-ml/tianshou)
and [armscan_env](https://github.com/appliedAI-Initiative/armscan_env/)

# Usage

## Prerequisites

The template supports python 3.11 and higher. For a smooth project generation you need to have

1) Cookiecutter. Install it e.g. with `pip install cookiecutter`
2) Poetry (for using the new repository)


## Creating a new project

Call

```shell script
cookiecutter https://github.com/appliedAI-Initiative/pymetrius -o path/to/directory
```

and walk through the questions. You can also clone this repository, adjust the template and call cookiecutter on
the local file.

You will get a repo in `<path/to/directory>/<project_name>`. For finalizing the setup, you can `cd` into it, and call
e.g.,

```shell script
git init
poetry shell
poetry install --with dev
poe format
git add . && git commit -m "Initial commit from pymetrius"
```

Note: if you want to use `sphinx-spelling`, as is configured by default in the `poe` tasks, you may need to install the `enchant` library,
see [installation instructions](https://pyenchant.github.io/pyenchant/install.html#installing-the-enchant-c-library). Otherwise, you
can just remove the spellcheck from the tasks.

Push to your branch and enjoy the fully setup pipelines and documentation!


# Contributing
The core maintainers are Michael Panchenko and Carlo Cagnetta at appliedAI. Initially, the project was also supported by Adrian Rumpold.
We are happy about any contribution to this project, feel free to contact us directly or to open an issue or a pull request.
