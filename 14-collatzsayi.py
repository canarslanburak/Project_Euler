import time
son_sayi=dict()
def collatz(sayi,son_sayi):
    deger=sayi
    adimlar=1
    while sayi !=1:
        if sayi in son_sayi:
            adimlar+= son_sayi[sayi]-1
            break
        if sayi%2==0:
            sayi//=2
            adimlar+=1
        else:
            sayi=3*sayi+1
            adimlar+=1
    son_sayi[deger]=adimlar
    return adimlar

start=time.time()
ebz=1
sayimiz=1
for i in range(1,1000000):
    adimsayisi=collatz(i,son_sayi)
    if adimsayisi>ebz:
        ebz=adimsayisi
        sayimiz=i

finish=time.time()
print(sayimiz,finish-start)