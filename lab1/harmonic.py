# Убедитесь, что гармонический ряд 1+½+⅓+... расходится (хотя общий его общий член 1/n стремится к нулю).
# Для этого напишите программу harmonic.py, которая для заданного числа a находит количество членов ряда такое,
# что их сумма превосходит a.


import math, sys
a = int(sys.argv[1])

n = 1
harm = n
while harm < a:
	n = n + 1
	harm = harm + 1/n

print(n)