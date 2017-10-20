#!/bin/bash

printf "\n\n\nTesting A*\n\n"
python3 a_star.py < testing/finalInput.txt | tee testing/finalOutput.txt

printf "\n\n\nTesting Naive\n\n"
python3 naive.py < testing/finalInput.txt | tee testing/finalOutput.txt
