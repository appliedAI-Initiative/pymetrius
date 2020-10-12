# {{cookiecutter.project_name}}

Welcome to the {{cookiecutter.project_name}} library!

Please open new issues for bugs, feature requests and extensions. See more details about the structure and
workflow in the [developer's readme](README-dev.md).

## Overview

Reports and source code documentation is published to your project's gitlab 
[pages](https://gitlab.aai.lab/{{cookiecutter.gitlab_project_path}}/pages)

## Installation

The library is published to our [package registry](https://nexus.admin.aai.sh/#browse/browse:aai-pypi). Install
it from there with
```shell script
pip install --extra-index-url https://nexus.admin.aai.sh/repository/aai-pypi/simple {{cookiecutter.project_name}}
```

To live on the edge, install the latest develop version with the `--pre` flag or install it directly from the
repo after cloning with

```python setup.py install```

from the root directory.
