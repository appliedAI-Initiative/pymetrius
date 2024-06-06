# {{cookiecutter.project_name}}

Welcome to the {{cookiecutter.project_name}} library!

## Getting Started

Clone the repository and run

```shell
git submodule update --init --recursive
```

to also pull the git submodules.

### Python setup

You can install the dependencies with

```shell
poetry install --with dev
```

### Docker setup

Build the docker image with

```shell
docker build -t {{cookiecutter.project_name}} .
```

and run it with the repository mounted as a volume:

```shell
docker run -it --rm -v "$(pwd)":/workspace {{cookiecutter.project_name}}
```

You can also just run `bash docker_build_and_run.sh`, which will do both things
for you.

Note: for the WSL subsystem on Windows you might need to adjust the path for the
volume.

### Codespaces

The fastest way to get started is to use a GitHub Codespace. Just click on the
button in the repository's main page.

## Contributing
Please open new issues for bugs, feature requests and extensions. See more details about the structure and
workflow in the [contributing page](docs/04_contributing/04_contributing.rst).
