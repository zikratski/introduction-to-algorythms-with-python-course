import sys
#TODO: do i need to reverse stack????
def getOrientedGraph(filename):
    res_dict = {}
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            cursities = line.strip('\n').split('\t')
            if cursities[0] in res_dict:
                res_dict[cursities[0]].append(cursities[1])
            else:
                res_dict[cursities[0]] = [cursities[1]]
    return res_dict

def topSort(graph):
    res_arr = list()
    visited_set= set()
    for vertex in graph:
        dfs_update(graph,vertex,visited_set, res_arr)
    res_arr.reverse()
    return res_arr

def dfs_update(graph, root, visited, stack_list):
    if root in visited:
        return
    visited.add(root)
    if root in graph:
        for neibghour in graph[root]:
            dfs_update(graph,neibghour,visited,stack_list)
    stack_list.append(root)

if __name__ == '__main__':
    filename = sys.argv[1]
    # filename = 'graph1.tsv'
    graph = getOrientedGraph(filename)
    # print(graph)
    sorted_graph = topSort(graph)
    print(sorted_graph)