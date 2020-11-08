import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_name = "{{cookiecutter.project_name}}"
project_url = "{{cookiecutter.project_url}}"

if not re.match(MODULE_REGEX, project_name):
    raise Exception(
        f"The project name {project_name} is not a valid Python module name"
    )

if not project_url.startswith("http"):
    raise Exception(f"project_url should start with http(s)://")
