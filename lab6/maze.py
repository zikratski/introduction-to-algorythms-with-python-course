import random
import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def getMatr(n,m):
    return [[1 for _ in range(n)]for _ in range(m)]
#m - строки, n - столбцы

def getMaze(matr,n,m):
    curm, curn = random.randrange(1,m-1),random.randrange(1,n-1)
    matr[curm][curn] = 0
    # print((curm,curn))
    neighs = [(curm, curn+2),(curm, curn-2),(curm+2, curn),(curm-2, curn)]
    neighs = list(filter(lambda ind: ind[0] >= 0 and ind[0] < m and ind[1] >= 0 and ind[1] < n, neighs))
    while neighs:
        cur = random.choice(neighs)
        matr[cur[0]][cur[1]] = 0
        curneighs = [(cur[0], cur[1]+2),(cur[0], cur[1]-2),(cur[0]+2, cur[1]),(cur[0]-2, cur[1])]
        random.shuffle(curneighs)
        curneighs = list(filter(lambda ind: ind[0] >= 0 and ind[0] < m and ind[1] >= 0 and ind[1] < n, curneighs))
        zero_cells = list(filter(lambda ind: matr[ind[0]][ind[1]] == 0, curneighs))
        join_cell = ((cur[0]+zero_cells[0][0])//2, (cur[1]+zero_cells[0][1])//2)
        matr[join_cell[0]][join_cell[1]] = 0
        neighs.remove(cur)
        neighs += list(filter(lambda ind: matr[ind[0]][ind[1]] != 0 and ind not in neighs, curneighs))
        # mazeToPlot(matr,m,n)
        # for i in neighs:
        #     matr[i[0]][i[1]] = 2


    return matr

def mazeToConsole(maze,m,n):
    maze = [''.join([str(j) if j == 1 else str(' ') for j in i]) for i in maze]
    for i in maze:
        print(i)

def mazeToPlot(maze, m,n):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.imshow(maze, cmap=plt.cm.gray_r)
    plt.show()
if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    # n = 4500
    # m =  4500
    matr = getMatr(n,m)
    # for i in matr:
    #     print(i)
    maze = getMaze(matr,n,m)
    mazeToConsole(maze,m,n)
    mazeToPlot(maze,n,m)
    # print(maze)
    # for i in maze:
    #     print(i)
    # print(maze)

