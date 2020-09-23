from setuptools import find_packages, setup

test_requirements = ["pytest"]
docs_requirements = [
    "Sphinx==2.4.2",
    "sphinxcontrib-websupport==1.2.0",
    "sphinx_rtd_theme",
]

setup(
    name="{{cookiecutter.package_name}}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    version="{{cookiecutter.initial_version}}",
    description="Library for {{cookiecutter.project_name}}",
    install_requires=open("requirements.txt").readlines(),
    setup_requires=["wheel"],
    tests_require=test_requirements,
    extras_require={"test": test_requirements, "docs": docs_requirements},
    author="{{cookiecutter.author}}",
)
