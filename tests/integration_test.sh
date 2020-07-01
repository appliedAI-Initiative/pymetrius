#!/usr/bin/env bash

# run this from the repository's top level directory

set -e

CLEANUP=false
OUTPUT_PATH=".."

while :; do
  case $1 in
  -o|-\?|--output)
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

  esac

done

OUTPUT_PATH=${1:-".."}

echo "Creating test project in $OUTPUT_PATH/inttest"
cookiecutter . --config-file  tests/config.yaml --no-input -o "$OUTPUT_PATH"
(
  echo "Building the testproject"
  cd "$OUTPUT_PATH/inttest"
  tox
  echo "SUCCESS"
  if $CLEANUP; then echo "Performing cleanup" && rm -rf ../inttest; fi
)

