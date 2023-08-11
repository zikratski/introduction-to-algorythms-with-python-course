# #Напишите программу matrixproduct.py, которая возвращает матричное произведение заданных матриц.
# # На входе может быть задано какое угодно количество матриц, которые передаются  строками вида  '-1 2 3, 4 -5 6, 7 8 -9'.
#
# Замечание: Перемножить матрицы A * B * С *...  можно только если количество столбцов A и строк B совпадает,
# количество столбцов B и строк C совпадает и т.д. Если матрицы несовместны, программа должна выводить сообщение
# ‘Error: incompatible sizes of matrices’. Если матриц нет, то выводится сообщение об ошибке ‘Error: invalid input’.



import sys

matrixes = sys.argv[1:]
intmatrixes = []
for i in matrixes:
    i = [r.strip() for r in i.split(',')]
    i = [[float(y) for y in z.split(' ')] for z in i]
    intmatrixes.append(i)

def mproduct(list_matr):
    if len(list_matr) == 0:
        return 'Error: invalid input'
    product = list_matr[0]
    for el in range(1,len(list_matr)):
            if len(product[0]) != len(list_matr[el]):
                return 'Error: incompatible sizes of matrices'
            else:
                newproduct = []
                for i in range(len(product)):
                    newproduct.append([])
                    for j in range(len(list_matr[el][0])):
                        newproduct[i].append(product[i][0] * list_matr[el][0][j])
                        #cdprint(newproduct[i][j])
                        for k in range(1,len(product[0])):
                            newproduct[i][j] += product[i][k] * list_matr[el][k][j]
                product = newproduct
    return product

print(mproduct(intmatrixes))