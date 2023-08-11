# Напишите программу power.py, которая для заданных a и n вычисляет an без использования системного возведения
# в степень, экспоненты и логарифма. Идея здесь в том, чтобы разбить исходное выражение на несколько более простых,
# которые можно вычислить рекурсивно, например, a100=(a50)(a50),a21=(a10)(a10)a.
# Таким образом, алгоритм сводится к следующим правилам: a2n=(a2)n; a2n+1=(a2)na; a0=1.

import sys

def power(a,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return power(a,n//2)*power(a,n//2)
    elif n%2 == 1:
        return power(a,n//2)*power(a,n//2)*a

if __name__ == '__main__':
    a = int(sys.argv[1])
    #a = -1
    n = int(sys.argv[2])
    #n = 5
    res = power(a,n)
    print(res)