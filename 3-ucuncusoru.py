def asalkontrol(deger):
    asaldir=True
    for i in range(2,int(deger**(0.5))+1):
        if(deger%i==0):
            asaldir=False
            continue
    return asaldir

sayi=600851475143
enb_asal=1
for i in range(2,int(sayi**(0.5))):
    if(sayi%i==0 and asalkontrol(i)):
        enb_asal=i
print(enb_asal)