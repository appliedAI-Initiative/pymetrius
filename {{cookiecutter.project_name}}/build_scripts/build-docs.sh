#!/usr/bin/env bash

set -euo pipefail

function usage() {
  cat > /dev/stdout <<EOF
Usage:
  build-docs.sh [FLAGS]

  Updates and builds the documentation. This script is executed during tox build.
  You can use this script directly to build/test docu without having to use tox as a middle man.

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
  python build_scripts/update_docs.py
  sphinx-build -W -b html -d "temp/doctrees" docs "docs/_build/html"
  sphinx-build -b doctest -d "temp/doctrees" docs "docs/_build/doctest"
)
