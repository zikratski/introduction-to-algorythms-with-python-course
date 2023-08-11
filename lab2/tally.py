# Напишите программу tally.py, которая для заданного на входе массива выводит
# матрицу [[элемент 1, кол-во в списке], [элемент 2, кол-во в списке], ...] (прямо как функция Tally в Mathematica).
# Элементы упорядочивать не нужно. Массив, как обычно, задается строкой.

import sys

mas = sys.argv[1]
mas = [int(s) for s in mas.split(',')]

def count(mas, n):
    num = 0
    for i in mas:
        if i == n:
            num +=1
    return num

def tall(mas):
    mas = [[i, count(mas, i)] for i in mas]
    #newmas = mas
    newmas = []
    for i in mas:
        if i not in newmas:
            newmas += [i]
    return newmas

print(tall(mas))