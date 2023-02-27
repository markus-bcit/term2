#!/bin/bash

if [[ $# -eq 0 ]]; then
  echo "Usage: ./script3.sh <file(s)>"
  exit 1
fi
for file in "$@"; do
	i=1 
	while read line; do  
	if [[ $i == 1 ]]; then
		echo $'\n'"File Name: $file"
	fi
		echo "$i : $line"  
		i=$((i+1))  
	done < $file
done