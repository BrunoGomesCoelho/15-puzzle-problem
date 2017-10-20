#!/bin/bash

printf "\n\n\nTesting A*\n\n"
python3 ../a_star.py < finalInput.txt | tee finalOutput.txt

printf "\n\n\nTesting Naive\n\n"
python3 ../naive.py < finalInput.txt | tee finalOutput.txt
