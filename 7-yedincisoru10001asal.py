import time

asal_adeti=0

def asalkontrol(sayi):
    asaldir=True
    if sayi==2:
        return True
    else:
        for i in range(2,int(sayi**(0.5))+1):
            if(sayi%i==0):
                asaldir=False
                continue
        return asaldir

sayi=2
baslangic=time.time()
while True:
    if asalkontrol(sayi):
        asal_adeti+=1
    if asal_adeti==100001:
        print(sayi)
        break
    sayi+=1
bitis=time.time()
print(bitis-baslangic)