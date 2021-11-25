from setuptools import find_packages, setup


def read_requirements(filename: str):
    return [line for line in open(filename).readlines() if not line.startswith("--")]


setup(
    name="{{cookiecutter.package_name}}",
    python_requires=">=3.8",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    version="{{cookiecutter.initial_version}}.dev1",
    description="{{cookiecutter.project_name}}",
    url="{{cookiecutter.project_url}}",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements-test.txt"),
        "docs": read_requirements("requirements-docs.txt"),
        "dev": read_requirements("requirements-dev.txt"),
        "linting": read_requirements("requirements-linting.txt"),
        "coverage": read_requirements("requirements-coverage.txt"),
    },
    author="{{cookiecutter.author}}",
)
