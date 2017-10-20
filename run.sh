#!/bin/bash

if [ $# != 1 ]; then
    echo "usage: $0 path_to_test_case"
else
    printf "\n\n\nA*\n\n"
    python3 a_star.py < $1

    printf "\n\n\nNaive\n\n"
    python3 naive.py < $1
fi


