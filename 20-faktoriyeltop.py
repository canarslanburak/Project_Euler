import math
from functools import reduce
""""n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!"""
def faktoriyel(deger=10):
    sonuc=math.factorial(deger)
    liste = [int(i) for i in str(sonuc)]
    print(reduce(lambda x, y: x + y, liste))
faktoriyel(100)
