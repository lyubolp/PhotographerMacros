#!/usr/bin/env bash

current_dir=$(pwd)
executable_dir=$(dirname $(realpath "$0"))

cd "$executable_dir" || exit

source .venv/bin/activate



if [[ -n $1 ]] && [[ $1 != -* ]] && stat "$1" >/dev/null 2>&1 
then
  first="$current_dir"/"$1"
else
  first="$1"
fi

if [[ -n $2 ]] && [[ $2 != -* ]] && stat "$2" >/dev/null 2>&1 
then
  second="$current_dir"/"$2"
else
  second="$2"
fi

shift 2

PYTHONPATH="$executable_dir" python3 src/main.py "$first" "$second" "$@"

deactivate