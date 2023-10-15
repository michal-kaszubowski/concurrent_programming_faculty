#!/bin/bash

input=$(</dev/stdin)

touch clientTry.txt
mv -n clientTry.txt lockFile

while [ -e clientTry.txt ]; do
    mv -n clientTry.txt lockFile
    echo "Waiting for server..."
done

$input > serverBuff.txt
