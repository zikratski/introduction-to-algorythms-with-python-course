import sys, collections

def actors_to_graph_movies(filename):
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
            # if actor == 'Aaron Eckhart':
            #     pass
            res_dict[actor] += [[file, actr] for actr in list(actors_set-{actor})]
    # print(res_dict)
    new_res_dict = {}
    for key,value in res_dict.items():
        new_res_dict[key] = []
        visited = []
        for item in value:
            if item[1] not in visited:
                visited.append(item[1])
                new_res_dict[key].append(item)

    return new_res_dict

def bfs_search_path(graph, root):
    visit_queue = collections.deque([root])
    dist = {}
    inf = float('inf')
    for key in graph.keys():
        dist[key] = [0, []] if key == root else [inf, []]
    # print(graph)
    while visit_queue:
        vertex = visit_queue.popleft()
        for neighbour in graph[vertex]:
            if dist[vertex][0] + 1 < dist[neighbour[1]][0]:
                dist[neighbour[1]][0] = dist[vertex][0] + 1
                dist[neighbour[1]][1] = dist[vertex][1] + [neighbour]
                # dist[neighbour[1]][1].append(neighbour[0])
                visit_queue.append(neighbour[1])
        mas = [[i, dist[i]] for i in dist.keys() if dist[i] != [inf, []]]
    return dist


if __name__ == '__main__':
    filename = sys.argv[1]
    actor_from = sys.argv[2]
    actor_to = sys.argv[3]
    # filename = 'actors.tsv'
    # actor_from = 'Kevin Bacon'
    # actor_to = 'Tom Hardy'
    graph = actors_to_graph_movies(filename)
    # lens = []
    # for i in graph:
    #     lens.append(len(graph[i]))
    # s = sum(lens)
    # print(s)
    # print(graph)
    data = bfs_search_path(graph, actor_from)[actor_to]
    print(f"distance: {data[0]}")
    print(f"{actor_from} was with {data[1][0][1]} in {data[1][0][0]}")
    for i in range(1,len(data[1])):
        print(f"{data[1][i-1][1]} was with {data[1][i][1]} in {data[1][i][0]}")