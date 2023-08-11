# Напишите программу palindrome.py, которая принимает на вход строку и проверяет,
# является ли она палиндромом. Для этого переверните строку при помощи рекурсии и сравните ее с оригиналом.

import sys

def palindr(n):
    if len(n) == 0:
        return n
    else:
        return palindr(n[1:]) + n[0]

if __name__ == '__main__':
    n = sys.argv[1]
    #n = '12343210'
    #print(palindr(n))
    if n == palindr(n):
        print(True)
    else:
        print(False)

