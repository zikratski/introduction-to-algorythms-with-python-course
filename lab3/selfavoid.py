import random
from matplotlib import pyplot as plt

def next_step(route :list, n:int):
    cur_route = route
   # print(cur_route)
    last_pos = cur_route[-1]
    #print(last_pos)
    allposible = [(last_pos[0]+1,last_pos[1]),(last_pos[0]-1,last_pos[1]),
                  (last_pos[0],last_pos[1]+1),(last_pos[0],last_pos[1]-1)]
    realposible =  [elem  for elem in allposible if -1<elem[0]<n+1
                    and -1<elem[1]<n+1 and elem not in cur_route]
    if len(realposible) == 0:
        return 0
    else:
        cur_route.append(random.choice(realposible))
        return cur_route
if __name__ == '__main__':
    n = 20
    line  = [(n//2, n//2)]
    while True:
        res = next_step(line, n)
        if res:
            line = res
        else:
            # print("NOOOOO")
            break
    # print(line)

    x = [elem[0] for elem in line]
    y = [elem[1] for elem in line]

    plt.plot(x, y)#'ko-')
    plt.scatter([x[0]],[y[0]],color = 'red',linewidths = 2)
    plt.scatter([x[-1]], [y[-1]], color='blue',linewidths = 2)
    plt.xlim([1,n])
    plt.ylim([1,n])
    ticks = [x for x in range(1, n + 1)]
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.grid()
    plt.show()