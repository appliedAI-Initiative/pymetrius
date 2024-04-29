import os
import shutil


def remove(filepath: str):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


def delete_line_in_file(filepath: str, line_starts_with: str):
    with open(filepath, "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if not line.strip().strip("\n").startswith(line_starts_with):
                f.write(line)
        f.truncate()


if "{{cookiecutter.include_readthedocs_yaml}}".lower() != "y":
    remove(".readthedocs.yaml")

if "{{cookiecutter.include_accsr_configuration_utils}}".lower() != "y":
    remove("config.py")
    remove("config.json")
    remove("docs/02_notebooks/02_config_example.ipynb")
    remove("data")
    delete_line_in_file("pyproject.toml", "accsr")
    delete_line_in_file(".gitignore", "config_local.json")

return_code = os.system("""
echo "Initializing your new project in $(pwd)."

git init
"""
)
if return_code:
    import sys
    sys.exit(return_code)
