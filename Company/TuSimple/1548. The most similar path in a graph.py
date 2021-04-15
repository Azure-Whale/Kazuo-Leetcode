class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        # The solution below is brute force, find all path and compare them with the targetPath until you get the path having minimal diff
        # Time: V(E+V) V is number of names, E is number of roads
        # It can be optimized by dp, dp[i][v] means path having length i and ending with V and mininal path   dp[i][v] = min(dp[i-1][u],cost(v)) so that you don't have to 
        # iterate all paths
        # https://leetcode.com/problems/the-most-similar-path-in-a-graph/

        graph  = [[] for x in range(len(names))]

        for road in roads:
            location, target = road
            graph[location].append(target)
            graph[target].append(location)
        
        target_length = len(targetPath)
        
        t= []
        def DFS(head,path,cost):
            path.append(head)
            cost += names[head]!=targetPath[(len(path) - 1)]
            if len(path) == target_length:
                paths[cost] = path
                return
            
            for node in graph[head]:
                temp = path.copy()
                DFS(node,temp,cost)

        paths = dict()
        
        for head in range(len(names)):
            DFS(head,[],0)
        return paths[min(paths)]