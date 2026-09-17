#!/bin/bash

printf "Beginning installation\n"

printf "Cleaning up old installations\n"
rm -rf .venv
# rm -f jsonFormat_pb2*
rm -rf logs
printf "This script does not clean the local_data folder automatically\n"

PYTHON_VER="python"
PIP_VER="pip"

if command -v python3 >/dev/null 2>&1; then
  PYTHON_VER="python3"
  PIP_VER="pip3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_VER="python"
  PIP_VER="pip"
elif command -v py >/dev/null 2>&1; then
  PYTHON_VER="py"
  PIP_VER="py -m pip"
else
  printf "Installation incomplete, no python found.\n"
  exit
fi

$PYTHON_VER -m venv .venv
if [ "$(uname)" == "Linux" ]; then
  source .venv/bin/activate
elif [ $OSTYPE == "msys" ]; then
  source .venv/Scripts/activate
fi

printf "Creating ./logs folder and ./logs/pip.log file\n"
mkdir logs
touch logs/pip.log
mkdir local_data
touch local_data/users_plaintext.csv
echo "username,password_plaintext,cancel_time" > local_data/users_plaintext.csv
mkdir local_data/puzzle_history

printf "Installing required packages with pip\n"
$PIP_VER install chess pandas > logs/pip.log
cd src
cd ..
printf "Installation complete\n\n"