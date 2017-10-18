#!/bin/bash

echo "Trivial case"
printf "A_star: "  # used printf here because there is the option of not putting \n
python3 a_star.py < cases/dummie.txt | tee outputs/trivialStar.txt
printf "Backtracking: "
python3 backtracking.py < cases/dummie.txt | tee outputs/trivialBacktracking.txt
printf "BFS: "
python3 naive.py < cases/dummie.txt | tee outputs/trivialNaive.txt

echo "Hard case"
printf "A_star: "  # used printf here because there is the option of not putting \n
python3 a_star.py < cases/takesALotOfTime.txt | tee outputs/hardStar.txt
printf "Backtracking: "
python3 backtracking.py < cases/takesALotOfTime.txt | tee outputs/hardBacktracking.txt
printf "BFS: "
python3 naive.py < cases/itakesALotOfTime.txt | tee outputs/hardNaive.txt


echo "Big case"
printf "A_star: "  # used printf here because there is the option of not putting \n
python3 a_star.py < cases/input100.txt | tee outputs/bigStar.txt
printf "Backtracking: "
python3 backtracking.py < cases/input100.txt | tee outputs/bigBacktracking.txt
printf "BFS: "
python3 naive.py < cases/input100.txt | tee outputs/bigNaive.txt
