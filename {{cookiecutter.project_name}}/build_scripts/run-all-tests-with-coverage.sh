#!/usr/bin/env bash

set -euo pipefail

function usage() {
  cat > /dev/stdout <<EOF
Usage:
  run-all-tests-with-coverage.sh [FLAGS]

  Creates the coverage report and the associated badge. This script is executed during tox build.
  You can use this script directly to create the coverage report without having to use tox as a middle man.

  Optional flags:
    -h, --help              Show this information and exit
EOF
}

while [[ $# -gt 0 ]]
do
  key="$1"
  case $key in
      -h|--help)
        usage
        exit 0
      ;;
      -*)
        >&2 echo "Unknown option: $1"
        usage
        exit 255
      ;;
      *)
        >&2 echo "This script takes no positional arguments but got: $1"
        exit 255
      ;;
  esac
done

BUILD_DIR=$(dirname "$0")

(
  cd "${BUILD_DIR}/.." || (echo "Unknown error, could not find directory ${BUILD_DIR}" && exit 255)
  coverage erase
  pytest --cov --cov-append --cov-report=term-missing tests
# IMPORTANT: this is flaky, sometimes the parallel execution can cause a KernelDied error
# this is due to the following unresolved issue: https://github.com/jupyter/nbconvert/issues/1066
# The current "solution" is to just restart the test execution / CI pipeline
  pytest -n auto notebooks
)
