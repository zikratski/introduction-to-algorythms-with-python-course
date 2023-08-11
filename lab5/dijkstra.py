import sys


def file_to_graph_weight(filename: str):
    res = {}
    with open(filename, encoding='utf-8') as f:
        while True:
            curline = f.readline()
            if curline:
                cursities = curline.split()[:2]
                curdist = float(curline.split()[2])
                for city in cursities:
                    if city not in res:
                        res[city] = []
                res[cursities[0]].append((cursities[1], curdist))
                res[cursities[1]].append((cursities[0], curdist))
            else:
                break
    return res

def djakstra(graph:dict,vertex):
    visited = set()
    dist = {elem: -1 for elem in graph.keys()}
    dist[vertex] = 0
    # arr = sorted([elem for elem in list(dist.items()) if elem[1] != -1 and elem[0] not in visited],
    #                         key= lambda a: a[1])[0]
    while len(visited) < len(graph.keys()):
        curlist = [elem for elem in list(dist.items()) if elem[1] != -1 and elem[0] not in visited]
        cur_vertex = sorted([elem for elem in list(dist.items()) if elem[1] != -1 and elem[0] not in visited],
                            key= lambda a: a[1])[0][0]
        for neighmour in graph[cur_vertex]:
            if neighmour in visited:
                continue
            if dist[neighmour[0]] == -1:
                dist[neighmour[0]] = dist[cur_vertex]+neighmour[1]
            elif dist[cur_vertex] + neighmour[1] < dist[neighmour[0]]:
                dist[neighmour[0]] = dist[cur_vertex] + neighmour[1]
        visited.add(cur_vertex)
        #     print(neighmour)
        # print("ok")
        # print('dsfdds')
    return dist


if __name__ == '__main__':
    filename = sys.argv[1]
    city = sys.argv[2]
    a = file_to_graph_weight(filename)
    b = djakstra(a, city)
    sortb = sorted(b.items(), key = lambda x:x[1])
    print('Top 5 nearest cities:')
    for i in range(5):
        print(sortb[i+1])
    print('Top 5 distant cities:')
    for i in range(5):
        print(sortb[len(sortb)-5+i])
