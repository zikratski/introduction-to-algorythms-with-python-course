import sys, collections

def getGraph(file):
    res_dict = {}
    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            cursities = line.strip('\n').split('\t')
            for city in cursities:
                if city not in res_dict:
                    res_dict[city] = list(set(cursities) - {city})
                else:
                    res_dict[city] += list(set(cursities) - {city})
    return res_dict
        # while True:
        #     curline = f.readline()
        #     if curline:
        #         cursities = curline.strip("\t")
        #         for city in cursities:
        #             if city not in res_dict:
        #                 res_dict[city] = set(cursities) - set(city)
        #     else:
        #         break

def bfsSearch(graph, root):
    # visit_queue = collections.deque([root])
    # dist = {}
    # inf = float('inf')
    # for key in graph.keys():
    #     dist[key] = 0 if key == root else inf
    # while visit_queue:
    #     vertex = visit_queue.popleft()
    #     for neighbour in graph[vertex]:
    #         if dist[vertex] + 1 < dist[neighbour] or dist[neighbour] == -1:
    #             dist[neighbour] = dist[vertex] + 1
    #             visit_queue.append(neighbour)
    # return dist
    q = collections.deque([root])
    visited = [root]
    while q:
        vertex = q.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)

    return visited


if __name__ == '__main__':
    file = sys.argv[1]
    vert = sys.argv[2]
    # file = 'cities.tsv'
    # vert = 'Полоцк'
    graph = getGraph(file)
    # print(graph)
    distances = bfsSearch(graph, vert)
    print(distances)