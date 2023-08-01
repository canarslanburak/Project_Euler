import math

def grid(sayi=2):
    tümdurum=math.factorial(2*sayi)
    tekrarlidurum=(math.factorial(sayi))**2
    return tümdurum//tekrarlidurum
print(grid(20))
