from setuptools import find_packages, setup

test_requirements = ["pytest"]

setup(
    name="{{cookiecutter.package_name}}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    version="{{cookiecutter.initial_version}}-dev1",
    description="Library for {{cookiecutter.project_name}}",
    install_requires=[
        line
        for line in open("requirements.txt").readlines()
        if not line.startswith("--")
    ],
    setup_requires=["wheel"],
    tests_require=test_requirements,
    author="{{cookiecutter.author}}",
)
