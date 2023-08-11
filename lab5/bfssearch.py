

import sys, collections
def actors_to_graph(filename):
    films_dict = {}
    res_dict = {}
    with open(filename, 'r', encoding='utf8') as f:
        while True:
            curline = f.readline()
            if curline:
                curline_splitted = curline.split('\t')
                actor, file = curline_splitted[0], curline_splitted[1].strip()
                if actor not in res_dict:
                    res_dict[actor] = []
                if file not in films_dict:
                    films_dict[file] = [actor]
                else:
                    films_dict[file].append(actor)

            else:
                break
    for file, actors in films_dict.items():
        actors_set = set(actors)
        for actor in actors:
            res_dict[actor] += list(actors_set.difference(actor))
    for key in res_dict.keys():
        res_dict[key] = list(set(res_dict[key]))
    return res_dict

def bfs_search(graph, root):
    visit_queue = collections.deque([root])
    dist = {}
    inf = float('inf')
    for key in graph.keys():
        dist[key] = 0 if key == root else inf
    while visit_queue:
        vertex = visit_queue.popleft()
        for neighbour in graph[vertex]:
            if dist[vertex] + 1 < dist[neighbour]:
                dist[neighbour] = dist[vertex] + 1
                visit_queue.append(neighbour)
    return dist


if __name__ == '__main__':
    filename = sys.argv[1]
    actor_from = sys.argv[2]
    actor_to = sys.argv[3]
    # filename = 'actors.tsv'
    # actor_from = 'Kevin Bacon'
    # actor_to = 'Tom Hardy'
    graph = actors_to_graph(filename)
    # print(graph)
    # with open('new.txt','w',encoding='utf-8') as f:
    #     for i in graph:
    #         f.write(f"{i}:{graph[i]}")
    cgraph = bfs_search(graph, actor_from)
    print(cgraph[actor_to])