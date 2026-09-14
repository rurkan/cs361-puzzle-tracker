#!/bin/bash

# IF LINUX:
# if [ "$(uname)" == "Linux" ]; then
python3 -m venv .venv
source .venv/bin/activate
# fi

printf "Beginning installation\n"
# python3 -m venv venv
# Cleanup of any previous install
printf "Cleaning up old installations\n"
rm -f jsonFormat_pb2*
rm -rf logs

printf "Creating ./logs folder and ./logs/pip.log file\n"
mkdir logs
touch logs/pip.log
mkdir local_data
touch local_data/users_plaintext.csv
echo "username,password_plaintext" > local_data/users_plaintext.csv
touch local_data/user_info.csv
mkdir local_data/puzzle_history

# pip3 install grpcio grpcio-tools chess > logs/pip.log
pip3 install chess pandas
cd src
# python3 -m grpc_tools.protoc -I ../proto --python_out=. --grpc_python_out=. ../proto/jsonFormat.proto
cd ..
# echo -e "\nRun the following command to start Python Virtual Environment: \nsource .venv/bin/activate\n"
printf "Installation complete\n\n"