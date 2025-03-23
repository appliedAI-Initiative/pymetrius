import os
import shutil
import tomli
import tomli_w


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


def read_toml(filepath: str):
    """Read a TOML file."""
    with open(filepath, "rb") as f:
        return tomli.load(f)


def bump_semver(version: str, part: str = "minor") -> str:
    """
    Bump a semantic version string.

    Args:
        version: A semantic version string (e.g., '3.8.0')
        part: Which part to bump ('major', 'minor', or 'patch')

    Returns:
        The bumped version string
    """
    parts = version.split(".")
    major, minor, patch = (
        int(parts[0]),
        int(parts[1]) if len(parts) > 1 else 0,
        int(parts[2]) if len(parts) > 2 else 0,
    )

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1

    return f"{major}.{minor}.{patch}"


def update_pyproject_toml():
    """Update pyproject.toml with project config and dependencies."""
    project_config = read_toml("project_config.toml")
    dependencies = read_toml("dependencies.toml")

    # Read the current pyproject.toml
    with open("pyproject.toml", "rb") as f:
        pyproject = tomli.load(f)

    package_manager = "{{cookiecutter.package_manager}}".lower()

    # Add project configuration
    if package_manager == "poetry":
        # Poetry uses tool.poetry for project metadata
        pyproject["tool"] = pyproject.get("tool", {})
        pyproject["tool"]["poetry"] = {
            "name": project_config["project"]["name"],
            "version": project_config["project"]["version"],
            "description": project_config["project"]["description"],
            "authors": project_config["project"]["authors"],
            "license": project_config["project"]["license"],
            "readme": project_config["project"]["readme"],
            "homepage": project_config["project"]["homepage"],
            "classifiers": project_config["project"]["classifiers"],
            "packages": [project_config["project"]["package_dir"]],
            "exclude": project_config["project"]["exclude"],
        }

        # Add dependencies
        pyproject["tool"]["poetry"]["dependencies"] = {
            "python": f"^{project_config['project']['python_version']}"
        }
        for name, version in dependencies["dependencies"].items():
            pyproject["tool"]["poetry"]["dependencies"][name] = f"^{version}"

        # Add dev dependencies
        pyproject["tool"]["poetry"].setdefault("group", {})
        pyproject["tool"]["poetry"]["group"]["dev"] = {
            "optional": True,
            "dependencies": {},
        }
        for name, version in dependencies["dev-dependencies"].items():
            if isinstance(version, dict):
                # Handle complex dependencies like black = {version = "23.7.0", extras = ["jupyter"]}
                pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"][name] = {
                    "version": f"^{version['version']}",
                    "extras": version.get("extras", []),
                }
            else:
                pyproject["tool"]["poetry"]["group"]["dev"]["dependencies"][name] = (
                    "*" if version == "*" else f"^{version}"
                )

    elif package_manager == "uv":
        # UV uses standard project metadata

        pyproject["project"] = {
            "name": project_config["project"]["name"],
            "version": project_config["project"]["version"],
            "description": project_config["project"]["description"],
            "authors": [
                {
                    "name": author.split("<")[0].strip(),
                    "email": author.split("<")[1].strip(">"),
                }
                for author in project_config["project"]["authors"]
            ],
            "license": {"text": project_config["project"]["license"]},
            "readme": project_config["project"]["readme"],
            "requires-python": f">={project_config['project']['python_version']}, <{bump_semver(project_config['project']['python_version'], 'minor')}",
            "classifiers": project_config["project"]["classifiers"],
        }

        # Add project URLs
        pyproject["project"]["urls"] = {
            "Homepage": project_config["project"]["homepage"]
        }

        # Add dependencies
        pyproject["project"]["dependencies"] = []
        for name, version in dependencies["dependencies"].items():
            pyproject["project"]["dependencies"].append(f"{name}>={version}")

        # Add dev dependencies
        pyproject["project"]["optional-dependencies"] = {"dev": []}
        for name, version in dependencies["dev-dependencies"].items():
            if isinstance(version, dict):
                # Handle complex dependencies
                ver_str = version.get("version", "*")
                if "extras" in version:
                    extras = ",".join(version["extras"])
                    pyproject["project"]["optional-dependencies"]["dev"].append(
                        f"{name}[{extras}]>={ver_str}"
                    )
                else:
                    pyproject["project"]["optional-dependencies"]["dev"].append(
                        f"{name}>={ver_str}"
                    )
            else:
                if version == "*":
                    pyproject["project"]["optional-dependencies"]["dev"].append(name)
                else:
                    pyproject["project"]["optional-dependencies"]["dev"].append(
                        f"{name}>={version}"
                    )

    elif package_manager == "pixi":
        # Pixi uses tool.pixi for dependencies
        pyproject["project"] = {
            "name": project_config["project"]["name"],
            "version": project_config["project"]["version"],
            "description": project_config["project"]["description"],
            "authors": [
                {
                    "name": author.split("<")[0].strip(),
                    "email": author.split("<")[1].strip(">"),
                }
                for author in project_config["project"]["authors"]
            ],
            "license": {"text": project_config["project"]["license"]},
            "readme": project_config["project"]["readme"],
            "requires-python": f">={project_config['project']['python_version']}, <{bump_semver(project_config['project']['python_version'], 'minor')}",
            "classifiers": project_config["project"]["classifiers"],
        }

        # Add project URLs
        pyproject["project"]["urls"] = {
            "Homepage": project_config["project"]["homepage"]
        }

        # Add dependencies
        pyproject["tool"] = pyproject.get("tool", {})
        pyproject["tool"]["pixi"] = {}
        pyproject["tool"]["pixi"]["dependencies"] = {}
        for name, version in dependencies["dependencies"].items():
            pyproject["tool"]["pixi"]["dependencies"][name] = f">={version}"

        # Add dev dependencies
        pyproject["tool"]["pixi"]["dev-dependencies"] = {}
        for name, version in dependencies["dev-dependencies"].items():
            if isinstance(version, dict):
                # Handle complex dependencies
                pyproject["tool"]["pixi"]["dev-dependencies"][name] = {
                    "version": f">={version['version']}",
                    "extras": version.get("extras", []),
                }
            else:
                pyproject["tool"]["pixi"]["dev-dependencies"][name] = (
                    "*" if version == "*" else f">={version}"
                )

    # Write the updated pyproject.toml
    with open("pyproject.toml", "wb") as f:
        tomli_w.dump(pyproject, f)

    # Clean up the template files
    remove("project_config.toml")
    remove("dependencies.toml")


if "{{cookiecutter.include_readthedocs_yaml}}".lower() != "y":
    remove(".readthedocs.yaml")

if "{{cookiecutter.include_accsr_configuration_utils}}".lower() != "y":
    remove("config.py")
    remove("config.json")
    remove("docs/02_notebooks/02_config_example.ipynb")
    remove("data")
    delete_line_in_file(".gitignore", "config_local.json")

# Update pyproject.toml with project config and dependencies
update_pyproject_toml()

# Initialize git repository
return_code = os.system(
    """
echo "Initializing your new project in $(pwd)."

git init
"""
)
if return_code:
    import sys

    sys.exit(return_code)
