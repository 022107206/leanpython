#!/bin/bash

a=1
while [ $a -lt 1000000 ]; do
    echo 'hello world' >> f1.txt
    let a=$a+1
done

