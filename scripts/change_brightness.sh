#!/bin/bash

cd qr
for j in *.png
do 
  convert -brightness-contrast 10x5 "$j" "$j"2
done