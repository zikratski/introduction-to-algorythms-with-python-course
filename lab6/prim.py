import sys
import time


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

def primAlg(graph):
    visited = set()
    ost_tree = []
    sums = 0
    vert = list(graph.keys())[0]
    # vert = 'Белыничи'
    visited.add(vert)
    while len(visited) < len(graph.keys()):
        cur_neighbours = []
        for elem in visited:
            neighbours = [(elem, n, w) for n, w in graph[elem] if n not in visited]
            cur_neighbours.extend(neighbours)
        cur_edge = sorted(cur_neighbours, key=lambda x:x[-1])[0]
        ost_tree.append(cur_edge)
        visited.add(cur_edge[1])
        sums += cur_edge[-1]
    return ost_tree, sums


if __name__ == '__main__':
    filename = sys.argv[1]
    # filename = 'belarus.tsv'
    st = time.time()
    graph = file_to_graph_weight(filename)
    # print(list(graph.keys())[0])
    min_tree = primAlg(graph)
    end = time.time()
    # print(graph)
    print(end-st, min_tree[-1], min_tree[0])
