import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


if "{{cookiecutter.include_readthedocs_yaml}}" != "y":
    remove(".readthedocs.yaml")


return_code = os.system("""
git init
echo "Initializing repository in $(pwd)"
echo "Creating and activating venv"
python -m venv ./venv
. venv/bin/activate
echo "Installing {{cookiecutter.project_name}} in editable mode into venv"
pip install -e .
echo "Installing development dependencies"
pip install -r requirements-dev.txt
echo "Performing Initial formatting"
black .
echo "Initial commit"
git add . && git commit -m "Initial commit by python_library_template"
echo "Running the sample script"
python scripts/run_sample.py
""")
