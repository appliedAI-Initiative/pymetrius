#!/usr/bin/env bash

set -euo pipefail

function usage() {
  cat > /dev/stdout <<EOF
Usage:
  build-linting-report.sh [FLAGS]

  Checks formatting and imports and creates the pylint report. This script is executed during tox build.
  You can use this script directly to build/test linting without having to use tox as a middle man.

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
  black --check .
  isort . --check --diff
  python build_scripts/run_pylint.py >>>(pylint-json2html -f jsonextended -o pylint.html)
)
