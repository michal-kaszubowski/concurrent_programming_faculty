#!/bin/bash

while true; do
    read -p "Enter a number: " input

    CLIENT_DATA_REQUEST="True"
    while [ "$SERVER_DATA_REQUEST" = "True" ]; do
        if [ "$DATA_TURN" != "0" ]; then
            CLIENT_DATA_REQUEST="False"
            while [ "$DATA_TURN" != "0" ]; do
                continue
            done
            CLIENT_DATA_REQUEST="True"
        fi
    done

    echo "$input" > data.txt

    CLIENT_DATA_REQUEST="False"
    DATA_TURN="1"

    CLIENT_RESULT_REQUEST="True"
    while [ "$SERVER_RESULT_REQUEST" = "True" ]; do
        if [ "$RESULT_TURN" != "0" ]; then
            CLIENT_RESULT_REQUEST="False"
            while [ "$RESULT_TURN" != "0" ]; do
                continue
            done
            CLIENT_RESULT_REQUEST="True"
        fi
    done

    result=`cat result.txt`

    CLIENT_RESULT_REQUEST="False"
    RESULT_TURN="1"

    echo "Result: $result"
done
