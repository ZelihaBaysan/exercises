#!/bin/bash

echo "Lütfen bir sayı giriniz"

read sayi

if [ "$sayi" -eq 0 ]; then
    echo "Girilen sayı 0'dir"
elif [ "$sayi" -gt 0 ]; then
    echo "Girilen sayı 0'dan büyüktür"
else
    echo "Girilen sayı 0'dan küçüktür"
fi
