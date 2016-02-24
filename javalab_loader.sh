#!/bin/bash

value=$(<$1)

mkdir "repos"
cd "repos"

while read -r line; do
  arrIn=(${line//// })
  name=${arrIn[2]}
  mkdir $name
  cd $name
  git clone $line
  cd ..
done <<< "$value"
