#!/bin/bash

value=$(<$1)

while read -r line; do
  git clone $line
done <<< "$value"
