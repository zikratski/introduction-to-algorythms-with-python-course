# Напишите программу spiralmatrix.py, которая для заданного n строит квадратную матрицу n*n,
# состоящую из чисел от 1 до n2 расположенных по спирали. Алгоритм должен работать рекурсивно.

import sys
def spiral(n, arr, matr, ij=0):
    if n == 2:
        matr[ij][ij] = arr[0]
        matr[ij][n - 1 + ij] = arr[1]
        matr[ij + n - 1][n - 1 + ij] = arr[2]
        matr[ij + n - 1][ij] = arr[3]
    elif n == 1:
        matr[ij][ij] = arr[0]
    else:
        # lenmas = 0
        for i in range(n-1):
            matr[ij][ij+i] = arr[i]
            matr[ij+i][n-1+ij] = arr[i + n-1]
            matr[ij+n-1][n-1+ij-i] = arr[i + 2*(n-1)]
            matr[ij+n-1-i][ij] = arr[i + 3*(n-1)]
            # lenmas+=4
            # print(arr[i + 3*(n-1)])
        spiral(n-2,arr[(n-1)*4:], matr,ij+1)
    return matr

def showSpiral(n,sp_func = 0):
    ar = [[0 for j in range(n)] for i in range(n)]
    arr = [i for i in range(1,n**2+1)]
    ar = spiral(n,matr =ar, arr=arr)
    #print(ar)
    for strok in ar:
        strok = ''.join([str(num)+'\t' for num in strok])
        print(strok)


if __name__ == '__main__':
    n = int(sys.argv[1])
    #n = 6
    showSpiral(n)
