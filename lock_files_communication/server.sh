#!/bin/bash

while true; do
    if [ -e lockfile ]; then
        data=`cat serverBuff.txt`
        echo ">> $data"
        rm lockfile
    fi
done
