# Напишите программу mergesort.py, которая реализует сортировку слиянием.
# На входе программа получает три целых числа n, m, k. Программа генерирует список длины n случайных целых чисел от 1 до m,
# сортирует его, после чего выводит время выполнения и k последних элементов отсортированного списка.

import sys,random
import time


def sortArr(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    left_part = sortArr(arr[:len(arr) // 2])
    right_part = sortArr(arr[len(arr) // 2:])
    l = r = t = 0
    temp = [0 for i in range(len(arr))]
    while l < len(left_part) and r < len(right_part):
        if left_part[l] <= right_part[r]:
            temp[t] = left_part[l]
            l += 1
        else:
            temp[t] = right_part[r]
            r += 1
        t += 1
    while l < len(left_part):
        temp[t] = left_part[l]
        l += 1
        t += 1
    while r < len(right_part):
        temp[t] = right_part[r]
        r += 1
        t += 1
    for i in range(len(arr)):
        arr[i] = temp[i]
    return arr


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    k = int(sys.argv[3])
    #n = 1000
    #m = 600
    #k = 4
    arr = [random.randrange(1,m+1) for i in range(n)]
    # print(arr)
    start = time.time()
    sortArr(arr)
    end = time.time()
    if k != 0:
        print(arr[-k:])
    print(end - start)