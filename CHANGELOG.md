# Changelog

## 23.10.2020

### Features

- Added support for local config in CI

### Fixes

- Black formatter now ignores the venv
- The directory data/raw is part of initial commit (hopefully) 

## 12.10.2020

### Features

- Improved support for dependencies in aAI python package index
- Remote is added on project creation
- Reduced requirements-dev for faster project creation

### Changes

- Dropped support for python 3.7
- Pylint output no longer shown in tox run

## 11.10.2020

### Features

- Added a changelog to the generated project
- config.py now uses the data-access library for the config classes

## 10.10.2020

### Features

- Testing with tox and pytest
- Optimized gitlab ci pipeline
- Automatically create documentation files on build
- Automatically execute notebooks and add rendered notebooks to documentation on build
- Release management of library (includes manual steps)
- Template for configuration management
- pylint and coverage as part of build, results published as pages

### Development:

- First entry in changelog. 
