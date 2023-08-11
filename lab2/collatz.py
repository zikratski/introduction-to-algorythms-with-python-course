# Напишите программу collatz.py, которая для заданного n (n=1 по умолчанию) строит последовательность
# 3n+1 и выводит количество элементов в этой последовательности, а также ее максимальный элемент.
# Последовательность строится следующим образом:
#
#     n -- первый член последовательности
#     если n чётное, то делим его на 2, а если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1) -- это
#     следующий член
#     повторяем те же действия снова и снова пока не получим 1 (гипотеза Коллатца состоит в том, что эта
#     последовательность сходится к 1 для любого n)
#
# Замечание: Максимальный элемент должен быть найден без использования встроенных функций (типа max).

import sys
try:
    n = int(sys.argv[1])
except:
    n = 1
def coltz(n):
    seqn = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
            seqn += [n]
        else:
            n = 3*n + 1
            seqn += [n]
    return seqn
def maxn(mas):
    max = mas[0]
    for i in mas:
        if i > max:
            max = i
    return max
print([len(coltz(n)), maxn(coltz(n))])