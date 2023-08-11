# Напишите программу permutations.py, которая приведенным выше рекурсивным способом генерирует все
# перестановки заданной строки (рассматривая ее как список) + также возвращает их количество.

import sys

def perm(st,lst = []):
    if len(st) == 2:
        return 2,[st[-1]+st[0],st[0]+st[-1]]
    newst = []
    for i in range(len(st)):
        #for j in perm(''.join(list(set(st)-{st[i]})))[1]:
        for j in perm(st[:i]+st[i+1:])[1]:
            #print(st[i]+j)
            # a = st[i]+j
            # print(a)
            newst.append(st[i]+j)
    return len(newst), newst
    #return [(st[i] + perm(list(set(st)-{st[i]}))) for i in range(len(st))]

if __name__ == '__main__':
    st = sys.argv[1]
    #  st = 'list'
    print(perm(st))
    #print(len(set(perm(st))))