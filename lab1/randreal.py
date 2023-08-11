# Напишите программу randreal.py, которая для заданных целых чисел a,b генерирует случайное вещественное число
# в диапазоне [a,b]. Из пакета random можно использовать только функцию random().


import sys, random
a, b = int(sys.argv[1]),int(sys.argv[2])
r = random.random()
print(abs(a-b)*r+min(a,b))