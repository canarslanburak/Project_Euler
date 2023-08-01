sayi=0
for i in range(999,99,-1):
    for j in range(999, 99, -1):
        stringcarpim=str(i*j)
        if(stringcarpim[::-1]==stringcarpim):
            if(i*j>sayi):
                sayi=i*j
                print([i], [j], sayi)
print(sayi)