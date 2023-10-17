#!/bin/bash

echo "Put text here and press ctrl+D when finished!"
input=$(cat)

echo -e "\n>> Sending to the server..."

touch clientTry.txt # Client tries to crate the lockfile
mv -n clientTry.txt lockFile # Client creates the lockfile if such doesn't already exist

while [ -e clientTry.txt ]; do
    mv -n clientTry.txt lockFile
    echo "Waiting for server..."
done

$input > serverBuff.txt
