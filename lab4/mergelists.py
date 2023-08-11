# Напишите программу mergelists.py, которая выполняет слияние двух отсортированных списков чисел,
# причем делает это за один проход по обоим спискам (сложность O(n)). Для заданного параметра n (n>=1
# программа генерирует два списка целых чисел от 0 до n длины random.randrange(1, n+1), после чего сортирует их
# встроенной функцией и производит слияние. На выходе программа выдает оба списка, а также объединенный список.

import sys,random
import time

def sortLists(maxl,minl):
    if len(minl) == 0:
        return maxl
    if maxl[0] < minl[0]:
        maxl, minl = minl, maxl
    return [minl[0]] + sortLists(maxl,minl[1:])

if __name__ == '__main__':
    # n = int(sys.argv[1])
    n = 1000
    list_1 = sorted([random.randrange(n) for i in range(random.randrange(1, n+1))])
    list_2 = sorted([random.randrange(n) for i in range(random.randrange(1, n+1))])
    #list_1 = [0, 9, 10]
    #list_2 = [3, 6, 9, 11, 12, 13, 13, 16]
    #stra = time.time()
    res = sortLists(list_1,list_2)
    #end = time.time()
    #print(end-stra)
    print(list_1)
    print(list_2)
    print(res)