#!/usr/bin/env bash

current_dir=$(dirname $(realpath "$0"))

cd "$current_dir" || exit

source .venv/bin/activate

PYTHONPATH="$current_dir"

python3 src/main.py "$@"

deactivate