#!/bin/bash

if ! [ -d "./.venv" ]; then
    printf "Virtual Environment does not exist, running install.sh\n\n"
    ./install.sh
fi


VENV_PYTHON="./.venv/bin/python3"
$VENV_PYTHON src/init.py