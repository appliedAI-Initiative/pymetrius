import os
import shutil


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

cicd_providers = {
    "gitlab": ".gitlab-ci.yml",
    "azure": "azure-pipelines.yml",
    "github": ".github"
}

selected_cicd_provider = '{{cookiecutter.cicd_provider}}'
cicd_providers.pop(selected_cicd_provider, None)
for non_selected_cicd_provider in cicd_providers.keys():
    remove(non_selected_cicd_provider)

if "{{cookiecutter.include_readthedocs_yaml}}" == "n":
    remove(".readthedocs.yaml")


return_code = os.system("""git init
python scripts/update_docs.py
git add .gitignore && git commit -m "Added gitignore"
git add . && git commit -m "Initial commit of python_library_template"
python scripts/run_sample.py
""")
