# Напишите программу hanoi.py, которая для заданного количества дисков n решает задачу о Ханойских башнях
# при помощи рекурсии. Результатом программы должен быть список кортежных пар: с какого колышка на какой переместить диск.

import sys
def hanoiSolver(n, fr, to, aux):
    if n == 1:
        return [(fr,to)]
    else:
        list1 = hanoiSolver(n-1,fr,aux,to)
        list2 = [(fr,to)]
        list3 = hanoiSolver(n-1, aux, to, fr)
        return list1+list2+list3

if __name__ == '__main__':
    n = int(sys.argv[1])
    #n = 3
    print(hanoiSolver(n,1,2,3))
