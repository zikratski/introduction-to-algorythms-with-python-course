# Напишите программу integralmc.py, в которой при помощи метода Монте-Карло вычисляется интеграл
# функции sin(x)/x на заданном отрезке [a, b]. Количество точек также является входным параметром.
# Замечание: Задайте функцию так, чтобы интеграл считался на любом отрезке, даже если он включает точку 0.


import sys
import random
from math import *

a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

if(a==b):
    print(0)
s = 0
for i in range(1, n+1):
    rand = random.uniform(a,b)
    if rand == 0:
        s += 1
        continue
    s += sin(rand)/rand


print((b-a)*s/n)
