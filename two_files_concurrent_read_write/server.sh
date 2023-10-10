#!/bin/bash

CLIENT_DATA_REQUEST="False"
SERVER_DATA_REQUEST="False"
CLIENT_RESULT_REQUEST="False"
SERVER_RESULT_REQUEST="False"

DATA_TURN="0"
RESULT_TURN="1"

while true; do
    SERVER_DATA_REQUEST="True"
    while [ "$CLIENT_DATA_REQUEST" = "True" ]; do
        if [ "$DATA_TURN" != "1" ]; then
            SERVER_DATA_REQUEST="False"
            while [ "$DATA_TURN" != "1" ]; do
                continue
            done
            SERVER_DATA_REQUEST="True"
        fi
    done

    data=`cat data.txt`

    SERVER_DATA_REQUEST="False"
    DATA_TURN="0"

    SERVER_RESULT_REQUEST="True"
    while [ "$CLIENT_RESULT_REQUEST" = "True" ]; do
        if [ "$RESULT_TURN" != "1" ]; then
            SERVER_RESULT_REQUEST="False"
            while [ "$RESULT_TURN" != "1" ]; do
                continue
            done
            SERVER_RESULT_REQUEST="True"
        fi
    done

    echo "$(($data * 2))" > result.txt

    SERVER_RESULT_REQUEST="False"
    RESULT_TURN="0"
done
