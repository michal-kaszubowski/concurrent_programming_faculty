#!/bin/bash

while true; do
    if [ -e lockfile ]; then
        dest=$(head -n 1 serverBuff.txt)
        # cont=$(tail -n +2 serverBuff.txt)
        read -p "Response: " $cont
        echo ">> $cont"
        echo "$cont" > "$dest"
        rm lockfile
    fi
done
