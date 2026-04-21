#!/bin/bash

count=1

while [ $count -le 3 ]
do
  echo "Count is $count"
  count=$((count+1))
done
