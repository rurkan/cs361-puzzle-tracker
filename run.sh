#!/bin/bash

if ! [ -d "./.venv" ]; then
    printf "Virtual Environment does not exist, running install.sh\n\n"
    ./install.sh
fi

PYTHON_VER="python"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_VER="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_VER="python"
elif command -v py >/dev/null 2>&1; then
  PYTHON_VER="py"
else
  printf "Python was not found, please install python.\n"
  exit 0
fi

if [ "$(uname)" == "Linux" ]; then
  source .venv/bin/activate
elif [ $OSTYPE == "msys" ]; then
  source .venv/Scripts/activate
fi

$PYTHON_VER src/init.py