# Напишите программу means.py, которая для заданного на входе массива целых положительных чисел вычисляет
# и выводит массив следующих значений (с точностью до двух знаков):
#
#     среднее геометрическое
#     среднее арифметическое
#     медиана
#     среднее квадратическое
#
# Все вычисления должны быть произведены без использования сторонних пакетов, включая math.
# Замечание: Передать массив в качестве параметра командной строки нельзя, поэтому передавайте его строкой
# (‘1,2,3,4,5’), а уже в программе конвертируйте строку в массив.

import sys

mas = sys.argv[1]
mas = [float(s) for s in mas.split(',')]
#mas = [float(s) for s in mas]
def geomn(mas):
    fact = 1
    for i in mas:
        fact = fact * i
    if fact < 0:
        return "Error"
    return round(fact ** (1 / len(mas)), 2)

def arifm(mas):
    summ = 0
    for i in mas:
        summ += i
    return round(summ/len(mas), 2)

def med(mas):
    mas = sorted(mas)
    #print(mas)
    if len(mas) % 2 != 0:
        return mas[len(mas) // 2]
    else:
        return (mas[len(mas) // 2] + mas[len(mas) // 2 - 1]) / 2


def qwadr(mas):
    summ = 0
    for i in mas:
        summ += i**2
    return round((summ/len(mas)) ** (1/2), 2)

print(geomn(mas), arifm(mas), med(mas), qwadr(mas))








