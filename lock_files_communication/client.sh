#!/bin/bash

echo "Put text here and press ctrl+D when finished!"
input=$(cat)

echo -e "\n>> Sending $input to the server..."

touch clientTry # Client tries to crate the lockfile
mv -n clientTry lockfile # Client creates the lockfile if such doesn't already exist

while [ -e clientTry ]; do # If Client couldn't create the lockfile:
    mv -n clientTry lockfile # Client tries to create the lockfile
    echo ">$ Waiting for server..."
done

pid=$$
echo -e "${pid}buff\n$input\E" > serverBuff.txt # If Client created lockfile
