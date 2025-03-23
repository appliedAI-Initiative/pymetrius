# Use the official Python image for the base image.
FROM python:{{cookiecutter.python_version}}-slim

# Set environment variables to make Python print directly to the terminal and avoid .pyc files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install system dependencies required for package manager and build tools.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install pipx.
RUN python3 -m pip install --no-cache-dir pipx \
    && pipx ensurepath

# Add local bin to the path
ENV PATH="${PATH}:/root/.local/bin"

{% if cookiecutter.package_manager == 'poetry' %}
# Install the latest version of Poetry using pipx.
RUN pipx install poetry

# Set the working directory
WORKDIR /workspaces/{{cookiecutter.project_name}}

# Copy the pyproject.toml and poetry.lock files (if available) into the image.
COPY pyproject.toml poetry.lock* /workspaces/{{cookiecutter.project_name}}/

RUN poetry install --with dev

# Entrypoint should be a shell in the workdir with poetry shell activated
ENTRYPOINT ["/bin/bash", "-c", "poetry install --with dev && poetry shell && $0 $@"]
{% elif cookiecutter.package_manager == 'pixi' %}
# Install the latest version of Pixi
RUN curl -fsSL https://pixi.sh/install.sh | bash
ENV PATH="${PATH}:/root/.pixi/bin"

# Set the working directory
WORKDIR /workspaces/{{cookiecutter.project_name}}

# Copy the pixi.toml file into the image.
COPY pixi.toml /workspaces/{{cookiecutter.project_name}}/

RUN pixi install

# Entrypoint should be a shell in the workdir with pixi shell activated
ENTRYPOINT ["/bin/bash", "-c", "pixi install && pixi shell && $0 $@"]
{% elif cookiecutter.package_manager == 'uv' %}
# Install the latest version of uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set the working directory
WORKDIR /workspaces/{{cookiecutter.project_name}}

# Copy the pyproject.toml file into the image.
COPY pyproject.toml /workspaces/{{cookiecutter.project_name}}/

# Create virtual environment and install dependencies
RUN uv pip install -e ".[dev]"
ENV PATH="/workspaces/{{cookiecutter.project_name}}/.venv/bin:${PATH}"

# Entrypoint to ensure environment is activated
ENTRYPOINT ["/bin/bash", "-c", "source .venv/bin/activate && $0 $@"]
{% endif %}
