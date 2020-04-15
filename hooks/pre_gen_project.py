import re

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

project_name = '{{cookiecutter.project_name}}'
host_url = '{{cookiecutter.host_url}}'

if not host_url.startswith("https://") or host_url.startswith("http://"):
    raise Exception(f"Invalid host url {host_url}, should start with https:// or http://")

if not re.match(MODULE_REGEX, project_name):
    raise Exception(f'The project name {project_name} is not a valid Python module name')
