import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.include_readthedocs_yaml}}" != "y":
    remove(".readthedocs.yaml")


# TODO: replace the line installing data-access one we have open sourced it under a new name
return_code = os.system(
    """
echo "Initializing your new project in in $(pwd). This might take a while"
git init
echo "Creating and activating venv"
python{{cookiecutter.python_version}} -m venv ./.venv
. .venv/bin/activate
echo "Installing formatter"
pip install -q black isort pre-commit
echo "Performing Initial formatting"
black .
isort .
echo "Setting git hooks"
pre-commit install
pre-commit autoupdate
echo "Initial commit"
git add . && git commit -q -m "Initial commit by python_library_template"
git branch develop && git checkout develop
echo "Installing {{cookiecutter.project_name}} in editable mode into venv"
pip install -q -e .
pip install -q --extra-index-url https://nexus.admin.aai.sh/repository/aai-pypi/simple data-access
echo "A virtual environment for your project has been created in $(pwd)/venv.\
 The library was installed there in editable mode."
echo "Running the sample script"
python scripts/run_sample.py
"""
)
if return_code:
    import sys
    sys.exit(return_code)
