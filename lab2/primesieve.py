# Напишите программу primesieve.py, которая для заданного n (по умолчанию n=10) выдает массив простых
# чисел от 2 до n просеиванием решета Эратосфена. Этот метод работает так:
#
#     сначала записываем все числа 2,3,4,5,...,n
#     первое число (2) будет простым -- вычеркиваем все, делящиеся на 2, остаются 3,5,7,9,...n
#     первое число (3) будет простым -- вычеркиваем все, делящиеся на 3,
#
#     остаются 5,7,11,...n
#     продолжаем в том же духе пока не просеем все числа

import sys

n = int(sys.argv[1])
#n = int(input())


def eratosph(n):
    masn = list(range(2, n+1))
    factmasn = []
    for i in masn:
        if i**2 <= max(masn):
            k = 2
            while(i*k <= max(masn)):
                factmasn.append(i * k)
                k +=1
        else:
            break
    #print(factmasn)
    masn = sorted(list(set(masn) - set(factmasn)))
    return masn

print(eratosph(n))
