echo "Lütfen 2 tane sayı giriniz"
read sayi1
read sayi2

if [ "$sayi1" -gt "$sayi2" ]; then
    echo "$sayi1"
elif [ "$sayi1" -lt "$sayi2" ]; then
    echo "$sayi2"
else
    echo "Sayılar eşit"
fi
