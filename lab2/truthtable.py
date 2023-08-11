# Для построения таблицы истинности какой-то логической функции, содержащей n переменных,
# нужно сначала построить таблицу всех возможных значений этих переменных (True/False).
# Напишите программу truthtable.py, которая для заданного n строит и выводит такую таблицу.
# Для простоты выводите не True/False, а 1/0.

import sys
n = int(sys.argv[1])

def binar(i, n):
    elem = []
    while(i > 0):
        elem += [i%2]
        i //= 2
    while len(elem) < n:
        elem.append(0)
    elem.reverse()
    #print(elem)
    return elem

for i in range(2**n-1,-1,-1 ):
    print(binar(i,n))

