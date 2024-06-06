#!/usr/bin/bash

docker build -t {{cookiecutter.project_name}} .

docker run -it --rm -v "$(pwd)":/workspace {{cookiecutter.project_name}}
