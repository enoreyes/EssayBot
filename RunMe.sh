#!/usr/bin/env bash
echo Please enter your text below.
read input
python3 checker.py "${input}"
python3 main.py --nsamples=3 --text "${input}" > out.txt
python3 fixer.py