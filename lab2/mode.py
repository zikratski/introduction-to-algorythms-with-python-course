# Напишите программу mode.py, которая для заданного на входе массива целых положительных чисел
# вычисляет моду, т.е. элемент, который встречается чаще всего. Программа должна вывести список,
# состоящий из одного или нескольких значений (если мод несколько).
# Замечание: Передать массив в качестве параметра командной строки нельзя, поэтому передавайте его
# строкой (‘1,2,3,4,5’), а уже в программе конвертируйте строку в массив.

import sys
#mas = input()
mas = sys.argv[1]
#mas = '1,2,3,4,5,6,7,8,9,1,2,5,6,1,2,1,2'
#x = '1,2,3,4,5,1,2,3,4,5,1,1,22,2,2,2'
#x = [int(s) for s in x.split(',')]
#print(x.count(1),x.count(2))
#print(mas.count(2))
mas = [int(s) for s in mas.split(',')]

def mode(mas):
    maxnum = 1
    endmas = []

    for i in mas:
        num = mas.count(i)
        if num >= maxnum and num >= 2 and i not in endmas:
            if num > maxnum:
                maxnum = num
                endmas.clear()
                endmas = [i]
            elif num == maxnum:
                endmas += [i]
    return endmas

print(mode(mas))