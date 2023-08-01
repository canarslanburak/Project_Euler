import math
import time
from functools import reduce
def rakamlartoplamı(üs):
    sayi = int(math.pow(2, üs))
    liste = [int(i) for i in str(sayi)]
    print(reduce(lambda x,y: x+y,liste))
baslangic=time.time()
rakamlartoplamı(1000)
bitis=time.time()
print(bitis-baslangic)