def asalkontrol(sayi): #Asalları kontrol etmek için bunu kullan
    asaldir=True
    if sayi==2:
        return True
    else:
        for i in range(2,int(sayi**(0.5))+1):
            if(sayi%i==0):
                asaldir=False
                break
        return asaldir
toplam=0
sayi=2
while True:
    if asalkontrol(sayi):
        toplam+=sayi
    if sayi==2000000:
        break
    sayi+=1
print(toplam)
