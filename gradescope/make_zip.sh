#!/usr/bin/env bash

# copy test file
cp ../test_*.py ./
cp -r ../result_logs/ ./

zip -r gradescope.zip setup.sh requirements.txt run_autograder run_tests.py test_*.py result_logs/

# remove test file
rm ./test_*.py
rm -rf ./result_logs/
