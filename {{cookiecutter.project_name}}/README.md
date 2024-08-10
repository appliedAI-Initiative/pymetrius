# {{cookiecutter.project_name}}

Welcome to the {{cookiecutter.project_name}} library!

## Getting Started

You can have a local poetry or docker-interpeter based setup. The repository is also 
configured to seamlessly working within a GitHub Codespace. See the instructions
for the various setup scenarios below.

Independently of how the setup was done, the virtual environment can be activated with
`poetry shell` and the various tasks like formatting, testing, and documentation building
can be executed using `poe`. For example, `poe format` will format the code, including the 
notebooks. Just run `poe` to see the available commands.

### Python (poetry) setup

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
