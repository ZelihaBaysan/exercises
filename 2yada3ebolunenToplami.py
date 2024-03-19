sum_list=[]
for i in range(100):
    if (i % 3 == 0 or i % 2 == 0):
        sum_list.append(i)
    else:
        pass
    
toplam=0
for item in sum_list:
    toplam+=item
print(toplam)