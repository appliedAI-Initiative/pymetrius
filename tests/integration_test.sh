#!/usr/bin/env bash

# run this from the repository's top level directory

# This will create a new project, run the build/test suite and cleanup everything, if so desired.

set -e

CLEANUP=false
OUTPUT_PATH=".."

while :; do
  case $1 in
  -o | -\? | --output)
    if [ "$2" ]; then
      OUTPUT_PATH=$2
      shift 2
    else
      echo 'ERROR: "-o/--output" requires a non-empty option argument.'
      exit 1
    fi
    ;;
  --cleanup)
    CLEANUP=true
    shift
    ;;
  --)
    shift
    break
    ;;
  -?*)
    printf 'WARN: Unknown option (ignored): %s\n' "$1" >&2
    ;;
  *)
    break
    ;;

  esac

done

OUTPUT_PATH=${1:-".."}

TESTPROJECT_NAME="python_library_template_output"

echo "Creating test project in $OUTPUT_PATH/$TESTPROJECT_NAME"
cookiecutter . --config-file tests/config.yaml --no-input -o "$OUTPUT_PATH"
(
  echo "Building $TESTPROJECT_NAME for the first time. This might take quite a while."
  cd "$OUTPUT_PATH/$TESTPROJECT_NAME"
  tox
  echo "SUCCESS"
  if $CLEANUP; then echo "Performing cleanup" && rm -rf "${OUTPUT_PATH:?}/${TESTPROJECT_NAME}"; fi
)
