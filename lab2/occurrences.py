# Напишите программу occurrences.py, которая для двух заданных  строк находит сколько раз вторая
# строка встречается в первой. Добейтесь того, чтобы поиск совершался за один проход по строке.
# Замечание: Поиск не должен учитывать регистр, т.е. строка ‘Th’ должна находиться в ‘thought’.

import sys

f1, f2 = sys.argv[1].lower(), sys.argv[2].lower()

def occ(f1,f2):
    count = 0
    for i in range(len(f1)):
        if f2 == f1[i:i+len(f2)]:
            count +=1
    return count

print(occ(f1,f2))