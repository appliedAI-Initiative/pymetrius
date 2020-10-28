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
Make sure that appliedAI's python package index can be resolved by pip. The simplest way to reach that is to
add a global pip configuration, for ubuntu in `~/.config/pip/pip.conf`:
```
[global]
extra-index-url = https://nexus.admin.aai.sh/repository/aai-pypi/simple
```


### Additional requirements

The main requirements for developping the library locall are in `requirements-dev.txt`.
For building documentation locally (which is done as part of the tox suite) you will need pandoc. 
It can be installed e.g. via
```shell script
sudo apt-get update -yq && apt-get install -yq pandoc
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

By default the configured secrets like access keys and so on are expected to be in a file called `config_local.json`.
In order for these secrets to be available in CI/CD during the build, _create a gitlab variable of type file called_
`CONFIG_LOCAL` containing your CI secrets. 
Note that sometimes it makes sense for them to differ from your own local config.

Generally the configuration utils support an arbitrary hierarchy of config files, you will have to adjust the
[config.py](config.py) and the gitlab pipeline if you want to make use of that.

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


#### Automatic release process

In order to create an automatic release, a few prerequisites need to be satisfied:

- The project's virtualenv needs to be active
- The repository needs to be on the `develop` branch
- The repository must be clean (including no untracked files)

Then, a new release can be created using the `build_scripts/release-version.sh` script (leave off the version parameter
to have `bumpversion` automatically derive the next release version):

```shell script
./scripts/release-version.sh 0.1.6
```

To find out how to use the script, pass the `-h` or `--help` flags:

```shell script
./build_scripts/release-version.sh --help
```

If running in interactive mode (without `-y|--yes`), the script will output a summary of pending
changes and ask for confirmation before executing the actions.

#### Manual release process
If the automatic release process doesn't cover your use case, you can also create a new release
manually by following these steps:

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
