#Напишите программу armstrong.py, которая для заданного целого числа n находит все числа Армстронга <= n.
# Число из k цифр называется числом Армстронга, если сумма его цифр, возведенных в k-ую степень, равна самому числу.
# Например, 153=13+53+33.

import sys
n = int(sys.argv[1])

def ksum(n):
    s = 0
    k = len(str(n))
    while n!= 0:
        s += (n % 10)**k
        n //= 10
    return s

def arm(n):
    armnumbs = []
    for i in range(1,n+1):
        if ksum(i) == i:
            armnumbs.append(i)
    return armnumbs

print(arm(n))