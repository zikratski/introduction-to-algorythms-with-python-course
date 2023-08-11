# На основе программы binary.py напишите программу baseform.py, которая для заданных числа и основания
# (от 2 до 10) выводит представление числа в этой системе счисления.

import sys

n = int(sys.argv[1])
a = int(sys.argv[2])
i = 0
while (a**(i+1) <= n):
        i = i + 1
s = ''
while (i >= 0):
        if (n - a**i >= 0):
                q = n//(a**i)
                n = n - q*a**i
                s = s + str(q)
        else:
                s = s + '0'
        i = i - 1
print(s)