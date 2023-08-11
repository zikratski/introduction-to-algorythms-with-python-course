import sys
import time

def giftTime(method):
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args,**kwargs)
        tend = time.time()
        return (result,'\n'+str(tend-ts))
    return timed
def getItems(filename):
    v = []
    w = []
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.split()
            v.append(int(line[0]))
            w.append(int(line[1]))
    return (v,w)
@giftTime
def knapsack_bottomup(v, w, W,n):
    v, w = v[:n], w[:n]
    sack = [[[0, []] for _ in range(W+1)] for _ in range(len(v))]
    sack[0] = [([v[0],[[v[0],w[0]]]] if i>=w[0] else [0,[]]) for i in range(len(sack[0]))]
    for ind,row in enumerate(sack[1:]):
        for indj,elem in enumerate(sack[ind+1]):
            if w[ind+1] > indj:
                sack[ind+1][indj][0] = sack[ind][indj][0]
                sack[ind+1][indj][1] = sack[ind][indj][1]
            else:
                sack[ind+1][indj][0] = max(sack[ind][indj][0], v[ind+1] + sack[ind][indj-w[ind+1]][0])
                a = [[v[ind+1],w[ind+1]]]
                b = sack[ind][indj - w[ind + 1]][1]
                if b == [] or type(b[0]) == int:
                    b = [b]+a
                else:
                    b.extend(a)
                candidates =  [sack[ind][indj], [v[ind+1] + sack[ind][indj-w[ind+1]][0],[i for i in b if i]]]
                candidate = list(filter(lambda x:x[0]==sack[ind+1][indj][0],candidates))[0]
                # if [] in candidate[1]:
                #     candidates[1] = candidates[1][:-2]
                # sack[ind+1][indj][1] = list(filter(lambda x:x==sack[ind+1][indj][0],
                #                                    [sack[ind][indj][1],sack[ind][indj-w[ind+1]][1].extend(a)]))[0]
                sack[ind + 1][indj][1] = candidate[1]



    return sack[-1][-1]

if __name__ == '__main__':
    # v = [1, 3, 2, 5, 6]
    # w = [2, 3, 2, 5, 6]
    # n = 10
    # W = 7
    filename = sys.argv[1]
    W = sys.argv[3]
    n = sys.argv[2]
    v, w = getItems(filename)[0],getItems(filename)[1]
    sack = knapsack_bottomup(v,w,W,n)

    print(sack[0],sack[1])
