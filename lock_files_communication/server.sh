#!/bin/bash

while true; do
    if [ -e lockFile ]; then
        data=`cat serverBuff`
        echo $data
done
