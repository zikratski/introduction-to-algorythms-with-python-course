import dijkstra,sys

def bellman(graph:dict,vertex):
    visited = set()
    inf = float('inf')
    dist = {elem: inf for elem in graph.keys()}
    dist[vertex] = 0
    for _ in range(len(graph)-1):
        for vert in graph:
            for neighbour in graph[vert]:
                if dist[neighbour[0]] > dist[vert] + neighbour[1]:
                    dist[neighbour[0]] = dist[vert] + neighbour[1]

    for vert in graph:
        for neighbour in graph[vert]:
            if dist[neighbour[0]] > dist[vert] + neighbour[1]:
                return "The graph has a cycle with negative weight"
    return dist

if __name__ == '__main__':
    filename = sys.argv[1]
    city = sys.argv[2]
    a = dijkstra.file_to_graph_weight(filename)
    # print(a)
    b = bellman(a, city)
    sortb = sorted(b.items(), key=lambda x: x[1])
    print('Top 5 nearest cities:')
    for i in range(5):
        print(sortb[i + 1])
    print('Top 5 distant cities:')
    for i in range(5):
        print(sortb[len(sortb) - 5 + i])