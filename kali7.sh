#!/bin/bash

max=0

echo "10 tane sayı giriniz"

for (( i=0; i<10; i++))
do
    read sayi
    if [ $sayi -eq 1 ]; then
        max=$sayi
    elif [ $sayi -gt $max ]; then 
        max=$sayi
    fi
done

echo "En büyük sayı: $max"
