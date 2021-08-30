#!/usr/bin/env bash

current_dir=$(pwd)
executable_dir=$(dirname $(realpath "$0"))

cd "$executable_dir" || exit

source .venv/bin/activate

PYTHONPATH="$executable_dir"

python3 src/main.py "$current_dir"/"$1" "$current_dir"/"$2" "$3"

deactivate