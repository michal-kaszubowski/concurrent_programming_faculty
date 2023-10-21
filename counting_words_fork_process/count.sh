#!/bin/bash

inputFile=$1
keyWord=$2
while IFS="" read -r p || [ -n "$p" ]; do
    if [ $(grep -ic "/input" <<< "$p") -ge 1 ]; then
        echo "Input!"
    else
        echo "No input."
    fi
done < "$inputFile"
