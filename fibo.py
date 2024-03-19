fibo = [1]
ilk = 1

for i in range(4000000):
    fibo.append(ilk)
    ilk += fibo[-2]

fibo2 = []

for sayi in fibo:  
    if sayi % 2 == 0:  
        fibo2.append(sayi)

sum = sum(fibo2)
print(sum)
