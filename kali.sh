echo "Lütfen bir değer giriniz"
read deger

if [ "$deger" -lt 0 ]; then
    echo "Sayının mutlak değeri $((deger * -1))"
else
    echo "Sayının mutlak değeri $deger"
fi
