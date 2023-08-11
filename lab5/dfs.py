import bfs, sys

def dfs(graph, root):
    visited, visited_set, visit_queue = list(), set(), list([root])
    while visit_queue:
        vertex = visit_queue.pop()
        if vertex in visited_set:
            continue
        visited.append(vertex)
        visited_set.add(vertex)
        # print(visited)
        visit_queue += graph[vertex]
    return visited

if __name__ == '__main__':
    file = sys.argv[1]
    vert = sys.argv[2]
    # file = 'cities.tsv'
    # vert = 'Полоцк'
    graph = bfs.getGraph(file)
    # print(graph)
    distances = dfs(graph,vert)
    print(distances)