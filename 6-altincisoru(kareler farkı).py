toplam1=0
toplam2=0
gecici=0
for i in range (1,101):
    toplam1=toplam1+(i**2)
    gecici=gecici+i
    toplam2=gecici**2
print(toplam2,"-",toplam1,"=",toplam2-toplam1)