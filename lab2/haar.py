# Напишите функцию haar.py, которая для заданного n (степень двойки) строит нормализованную матрицу
# Хаара (вы столкнетесь с ней в курсе вейвлет-анализа). Числа в матрице округлите до 3 знаков.
# Сама матрица имеет следующий вид:


import sys
import time

n = int(sys.argv[1])
#start = time.time()
#n = int(input())
def helpHaar(n):
    mas = []
    for i in range(n//2):
        mas.append(round(1/(n**(0.5)),3))
    for i in range(n//2,n):
        mas.append(round(-1 / (n ** (0.5)),3))
    return mas

def haar(n):
    matr = [[] for i in range(n)]
    matr[0] = [abs(i) for i in helpHaar(n)]
    matr[1] = helpHaar(n)
    i = 2
    twodeg = n
    while twodeg > 2:
        twodeg //= 2
        for ik in range(n // twodeg):
            matr[i] = [0 for i in range(n)]
            for k in range(ik*twodeg,ik*twodeg+len(helpHaar(twodeg))):
                matr[i][k] = helpHaar(twodeg)[k-ik*twodeg]
            i += 1


    return matr

#haar(n)
#end = time.time()
#print(f"время: {end-start}")
print(haar(n))
#ДЛЯ УДОБНОГО ПРОСМОТРА МОЖНО ИСПОЛЬЗОВАТЬ КОД НИЖЕ
#for i in haar(n):
#    print(i)
