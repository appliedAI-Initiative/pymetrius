#!/usr/bin/env bash

set -euo pipefail

## TTY colors and attributes
#normal=$(tput sgr0)                      # normal text
normal=$'\e[0m'                           # (works better sometimes)
bold=$(tput bold)                         # make colors bold/bright
red="$bold$(tput setaf 1)"                # bright red text
green=$(tput setaf 2)                     # dim green text
fawn=$(tput setaf 3); beige="$fawn"       # dark yellow text
yellow="$bold$fawn"                       # bright yellow text
darkblue=$(tput setaf 4)                  # dim blue text
blue="$bold$darkblue"                     # bright blue text
purple=$(tput setaf 5); magenta="$purple" # magenta text
pink="$bold$purple"                       # bright magenta text
darkcyan=$(tput setaf 6)                  # dim cyan text
cyan="$bold$darkcyan"                     # bright cyan text
gray=$(tput setaf 7)                      # dim white text
darkgray="$bold"$(tput setaf 0)           # bold black = dark gray text
white="$bold$gray"                        # bright white text


function fail() {
  echo "${red}$1${normal}"
  exit 1
}

function usage() {
  cat > /dev/stderr <<EOF
Usage:
  release-version.sh [FLAGS] VERSION_STR

  Optional flags:
    -d             Delete release branch after merging
    -v, --verbose  Print debug information
    -y, --yes      Do not prompt for confirmation, for non-interactive use

  Positional options:
    VERSION_STR   Version to release, e.g. v0.1.2.
                  If not specified, 'bumpversion' is used to determine release version number.

  Prerequisites:
    The repository has to be clean (including no untracked files) and on the ${bold}develop${normal} branch.
EOF
  exit 255
}

function _parse_opts() {
  POSITIONAL=()

  DEBUG=
  DELETE_BRANCH=
  FORCE_YES=

  while [[ $# -gt 0 ]]
  do
    key="$1"
    case $key in
        -v|--verbose)
          DEBUG=1
          shift
        ;;
        -y|--yes)
          FORCE_YES=1
          shift
        ;;
        -d|--delete-branch)
          DELETE_BRANCH=1
          shift
        ;;
        *)    # unknown option
          POSITIONAL+=("$1") # save it in an array for later
          shift
        ;;
    esac
  done

  export DEBUG
  export DELETE_BRANCH
  export FORCE_YES

  # Infer release version if none given
  if [[ -n "${POSITIONAL[*]}" ]]; then
    RELEASE_VERSION="${POSITIONAL[0]}"
  else
    RELEASE_VERSION="$(bump2version --dry-run --list release | grep new_version | sed -r s,"^.*=",,)"
  fi
  export RELEASE_VERSION
}

function _check_sanity() {
  # Make sure bumpversion can be executed
  if [[ -z $(command -v bumpversion) ]]; then
    fail "bumpversion not found on the path. Is the right virtualenv active?"
  fi

  # Validate we are currently in a clean repo
  if [[ -n $(git status --porcelain) ]]; then
    fail "Repository must be in a clean state."
  fi

  # Validate we are on the correct branch
  local BRANCH
  BRANCH=$(git rev-parse --abbrev-ref HEAD)
  if [[ "$BRANCH" != "develop" ]]; then
    fail "Repository must be on 'develop' branch, was on '$BRANCH'."
  fi
  unset BRANCH

  # Validate version string format
  if ! [[ $RELEASE_VERSION =~ [0-9]+\.[0-9]+\.[0-9] ]]; then
    fail "Invalid version string '$RELEASE_VERSION'"
  fi

  # Validate that tag doesn't exist yet
  if [[ -n $(git tag -l "$RELEASE_TAG") ]]; then
    fail "Tag for version already exists: ${bold}$RELEASE_TAG${normal}"
  fi
}

function _confirm() {
  cat << EOF
🔍 Summary of changes:
    - Create branch ${bold}$RELEASE_BRANCH${normal}
    - Bump version number: ${bold}$CURRENT_VERSION ⟶ $RELEASE_VERSION${normal}
    - Merge release branch into ${bold}master${normal}
    - Bump version number again to next development pre-release
    - Merge release branch into ${bold}develop${normal}
EOF
  if [[ -n "$DELETE_BRANCH" ]]; then
    echo "    - Delete release branch"
  fi

  echo -en "🚨️ ${yellow}Do you want to proceed? [y/N] ${normal}"
  read -n 1 -r
  echo
  if [[ ! ($REPLY =~ ^[Yy]$) ]]
  then
      echo "Nevermind."
      exit 255
  fi
}

_parse_opts "$@"
CURRENT_VERSION=$(bumpversion --dry-run --list patch | grep current_version | sed -r s,"^.*=",,)
RELEASE_BRANCH="release/v$RELEASE_VERSION"
RELEASE_TAG="v$RELEASE_VERSION"

if [[ -n "$DEBUG" ]]; then
  echo "DEBUG:           ${DEBUG}"
  echo "FORCE_YES:       ${FORCE_YES}"
  echo "RELEASE_BRANCH:  ${RELEASE_BRANCH}"
  echo "RELEASE_TAG:     ${RELEASE_TAG}"
  echo "CURRENT_VERSION: ${CURRENT_VERSION}"
  echo "RELEASE_VERSION: ${RELEASE_VERSION}"
fi

_check_sanity

if [[ -z "$FORCE_YES" ]]; then
  _confirm
fi

git pull --ff-only

echo "📝 Creating release branch"
git checkout -b "$RELEASE_BRANCH"
bumpversion --commit --new-version "$RELEASE_VERSION" release

echo "🔨 Merging release branch into master"
git checkout master
git pull --ff-only
git merge --no-ff -X theirs "$RELEASE_BRANCH"
git tag -a "$RELEASE_TAG" -m"Release $RELEASE_VERSION"
git push --follow-tags origin master

echo "🏷️ Bumping to next patch version"
git checkout "$RELEASE_BRANCH"
bumpversion --commit patch

echo "🔨 Merging release branch into develop"
git checkout develop
git merge --no-ff "$RELEASE_BRANCH"
git push origin develop

if [[ -n "$DELETE_BRANCH" ]]; then
  echo "🗑️ Deleting release branch"
  git branch -d "$RELEASE_BRANCH"
fi

echo -e "\U2728 All done! Get yourself some coffee and watch CI/CD pipelines for errors."
