graph = [[1,2,3],[0],[0],[0]]
num_nodes = len(graph)
# dfs, get path that iterated all nodes(number of iterated nodes = number of total nodes)
# using visited recording the nodes visited


def DFS(head,visited,path):
    path.append(head)
        #visited.add(head)
        #print(visited)
    if len(path) == num_nodes:
        ans.append(path)
        return

    for node in graph[head]:
        temp = path.copy()
        DFS(node,visited.copy(),temp)
    

ans = []
for i in range(len(graph)):
    visited = set()
    DFS(i, visited, [])
print(ans)
