#! /usr/bin/env bash
set -e

# Change current working directory to be the root, regardless of how this script is invoked
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

function test_app() {
  cd src || exit 1
}

function main() {
  test_app
}

main
