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
git add .gitignore && git commit -m "Added gitignore"
git add . && git commit -m "Initial commit of python_library_template"
echo "Repository initialized in $(pwd)"
python scripts/run_sample.py
""")
