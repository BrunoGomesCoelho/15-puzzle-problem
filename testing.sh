#!/bin/bash

echo "Trivial case"
printf "A_star: "  # used printf here because there is the option of not putting \n
python3 a_star.py < cases/dummie.txt > outputs/trivial.txt
printf "Backtracking: "
python3 backtracking.py < cases/dummie.txt > outputs/trivial.txt
printf "BFS: "
python3 naive.py < cases/dummie.txt > outputs/trivial.txt
