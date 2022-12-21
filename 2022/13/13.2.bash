#!/bin/bash

# 1  remove blank lines
# 2  remove [ and ]
# 3  add [[6]] and [[2]] to list as 6 and 2
# 4  sort numerically
# 5  enumerate every line (even blank ones)
# 6  find the lonely 2 and 6
# 7  cut off the 2 and 6, keeping line number (or index)
# 8  translate newlines into *
# 9  remove last extra * by cutting the line
# 10 let bc calculate the multiplication

(grep -v ^$ data.txt | tr -d "\[\]"; echo 6; echo 2) | sort -g | cat -n | grep -E '[^,][26]$'  | cut -f1 | tr '\n' '*' | cut -d'*' -f-2 | bc

