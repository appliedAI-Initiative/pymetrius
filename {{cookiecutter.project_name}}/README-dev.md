# {{cookiecutter.project_name}} development guide

This repository contains the {{cookiecutter.project_name}} python library together with utilities for building, testing, 
documentation and configuration management. 

This project uses the [black](https://github.com/psf/black) source code formatter
and [pre-commit](https://pre-commit.com/) to invoke it as a Git pre-commit hook.

When first cloning the repository, run the following command (after
setting up your virtualenv with dev dependencies installed, see below) to set up
the local Git hook:

```shell script
pre-commit install
```

## Local Development
Automated builds, tests, generation of docu and publishing are handled by cicd pipelines. 
You will find an initial version of the pipeline in this repo. Below are further details on testing 
and documentation. 

Before pushing your changes to the remote it is often useful to execute `tox` locally in order to
detect mistakes early on.

We strongly suggest to use some form of virtual environment for working with the library. E.g. with venv
(if you have created the project locally with the python-library-template, it will already include a venv)
```shell script
python -m venv ./venv
. venv/bin/activate
```
or conda:
```shell script
conda create -n {{cookiecutter.project_name}} python={{cookiecutter.python_version}}
conda activate {{cookiecutter.project_name}}
```
A very convenient way of working with your library during development is to install it in editable mode 
into your environment by running
```shell script
pip install -e .
```

### Testing and packaging
The library is built with tox which will build and install the package, run the test suite and build documentation.
Running tox will also generate coverage and pylint reports in html and badges. 
You can configure pytest, coverage and pylint by adjusting [pytest.ini](pytest.ini), [.coveragerc](.coveragerc) and
[.pylintrc](.pylintrc) respectively.

A note on notebooks: all notebooks in the [notebooks](notebooks) directory will be executed during test run, 
the results will be added to the docu in the _Guides and Tutorials_ section. Thus, notebooks can be conveniently used
as integration tests and docu at the same time.

You can run thew build by installing tox into your virtual environment 
(e.g. with `pip install tox`) and executing `tox`. 

For creating a package locally run
```shell script
python setup.py sdist bdist_wheel
```

### Documentation
Documentation is built with sphinx every time tox is executed, doctests are run during that step.
There is a helper script for updating documentation files automatically. It is called by tox on build and can 
be invoked manually as
```bash
python build_scripts/update_docs.py
```
See the code documentation in the script for more details on that.

Notebooks also form part of the documentation, see explanation above.

## Configuration Management
The repository also includes [configuration utilities](config.py) that are often helpful when using data-related libraries. 
They do not form part of the resulting package, you can (and probably should) adjust them to your needs.

## CI/CD and Release Process
This repository contains a [gitlab ci/cd pipeline](.gitlab-ci.yml) that will run the test suite and
publish docu, badges and reports. Badges can accessed from the pipeline's artifacts, e.g. for the coverage badge
the url will be:
```
https://gitlab.aai.lab/%{project_path}/-/jobs/artifacts/develop/raw/badges/coverage.svg?job=tox
```

### Development and Release Process

In order to be able to automatically release new versions of the package from develop and master, the
 CI pipeline should have access to the following variables (they should already be set on global level):

```
PYPI_REPO_URL
PYPI_REPO_USER
PYPI_REPO_PASS
```

They will be used in the release steps in the gitlab pipeline.

You will also need to set up Gitlab CI deploy keys for 
automatically committing from the develop pipeline during version bumping

A new release requires some manual work. Here is a description of the process:

1. (repeat as needed) implement features on feature branches merged into `develop`. 
Each merge into develop will advance the `.devNNN` version suffix and publish the pre-release version into the package 
registry. These versions can be installed using `pip install --pre`.
2. When ready to release: From the develop branch create the release branch and perform release activities 
(update changelog, news, ...). For your own convenience, define an env variable for the release version
    ```shell script
    export RELEASE_VERSION="vX.Y.Z"
    git checkout develop
    git branch release/${RELEASE_VERSION} && git checkout release/${RELEASE_VERSION}
    ``` 
3. Run `bumpversion --commit release` if the release is only a patch release, otherwise the full version can be specified 
using `bumpversion --commit --new-version X.Y.Z release` 
(the `release` part is ignored but required by bumpversion :rolling_eyes:).
4. Merge the release branch into `master`, tag the merge commit, and push back to the repo. 
The CI pipeline publishes the package based on the tagged commit.

    ```shell script
    git checkout master
    git merge --no-ff release/${RELEASE_VERSION}
    git tag -a ${RELEASE_VERSION} -m"Release ${RELEASE_VERSION}"
    git push --follow-tags origin master
    ```
5. Switch back to the release branch `release/vX.Y.Z` and pre-bump the version: `bumpversion --commit patch`. 
This ensures that `develop` pre-releases are always strictly more recent than the last published release version 
from `master`.
6. Merge the release branch into `develop`:
    ```shell script
    git checkout develop
    git merge --no-ff release/${RELEASE_VERSION}
    git push origin develop
    ```
6. Delete the release branch if necessary: `git branch -d release/${RELEASE_VERSION}`
7. Pour yourself a cup of coffee, you earned it! :coffee: :sparkles:

## Useful information

Mark all autogenerated directories as excluded in your IDE. In particular docs/_build and .tox should be marked 
as excluded in order to get a significant speedup in searches and refactorings.

If using remote execution, don't forget to exclude data paths from deployment (unless you really want to sync them)
