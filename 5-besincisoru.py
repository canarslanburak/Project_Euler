import math
import functools

def ebob(x,y):
    return math.gcd(x,y)
def ekok(x,y):
    return (x*y)//ebob(x,y)
sayilar=range(1,21)
sonuc=functools.reduce(ekok,sayilar)
print(sonuc)