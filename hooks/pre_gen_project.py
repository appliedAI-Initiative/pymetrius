import re

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_name = "{{cookiecutter.project_name}}"
project_url = "{{cookiecutter.project_url}}"

if not re.match(MODULE_REGEX, project_name):
    raise Exception(
        f"The project name {project_name} is not a valid Python module name"
    )

if project_url.startswith("http"):
    raise Exception(
        f"project_url should not start with http. "
        f"E.g. type github.com/name instead of https://github.com/name"
    )