# Напишите программу integraltrap.py, которая вычисляет интеграл функции ArcTan(x)/x по методу трапеций.
# Здесь отрезок также разбивается на равные интервалы, но приближение ведется не прямоугольниками, а трапециями,
# как показано на рисунке.

import math, sys
a,b,n = float(sys.argv[1]),float(sys.argv[2]), int(sys.argv[3])

def atang(x):
    return 1 if x == 0 else math.atan(x)/x
def intatan(a: float, b: float, n = 1000):
    size = abs(b - a)/n
    intervals = [(a+size*i, a+size*(i+1)) for i in range(n)]
    #print(intervals)
    res = [((atang(elem[0]) + atang(elem[1]))/2)*(size) for elem in intervals]
    return sum(res)

print(intatan(a,b,n))