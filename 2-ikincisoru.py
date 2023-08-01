f_sonraki=0
f_onceki=1
f_simdi=1
toplam=0
while f_sonraki < 4000000:
    f_sonraki=f_onceki+f_simdi
    if(f_sonraki%2==0):
        toplam+=f_sonraki
        #print(toplam) baştan sona çift toplamlar
    f_onceki=f_simdi
    f_simdi=f_sonraki
print(toplam)