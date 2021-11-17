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

if "{{cookiecutter.include_configuration_utils}}".lower() != "y":
    remove("config.py")
    remove("config.json")
    remove("notebooks/config_example.ipynb")
    delete_line_in_file("requirements-dev.txt", "accsr")
    delete_line_in_file("requirements-test.txt", "accsr")
    delete_line_in_file(".gitignore", "config_local.json")

return_code = os.system(
    """
echo "Initializing your new project in in $(pwd). This might take a while"

# THIS IS A NAIVE HACK TO PREVENT COOKIECUTTER FROM RENDERING IN GITHUB WORKFLOWS
cat .github/workflows/tox-addition.yaml >> .github/workflows/tox.yaml
rm .github/workflows/tox-addition.yaml

git init
echo "Creating and activating venv"
python{{cookiecutter.python_version}} -m venv ./.venv
. .venv/bin/activate
echo "Installing dev requirements"
pip install -q -r requirements-dev.txt
echo "Performing Initial formatting"
black . && isort . && nbstripout notebooks/*
echo "Setting git hooks"
pre-commit install
pre-commit autoupdate
echo "Initial commit"
git checkout -b develop
git add . && git add -f data/raw/hello.txt 
git commit -q -m "Initial commit by python_library_template"
echo "Installing {{cookiecutter.project_name}} in editable mode into .venv"
pip install -q -e .
echo "A virtual environment for your project has been created in $(pwd)/.venv, \
 the library was installed there in editable mode."
echo "Running the sample script"
python scripts/run_sample.py
echo "All done, you can start by running tox (will take a while the first time) and looking at the docu in \
  docs/_build/html. \n \
  You can also just quickly run tests and build the docu using \n \
  ./build_scripts/build-docs.sh \n \"
"""
)
if return_code:
    import sys
    sys.exit(return_code)
