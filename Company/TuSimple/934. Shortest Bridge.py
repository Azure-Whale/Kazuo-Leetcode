#https://leetcode.com/problems/shortest-bridge/

"""
Time Complexity O(row*col) as we used BFS and DFS to get components and 
Find the shortest path between two objects
1. using DFS/BFS find nodes for two objects in the matrix respectively
2. Start from any nodes in either object, using BFS and DP to get the distance between source object and end object
3. once the BFS reaches any node in end object, this should be the shortest path
"""

import collections

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        # using dfs to get two objects
        ROW = len(A)
        COL = len(A[0])
        
        
        def find_neighors(row,col):
            
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            neightbors = []
            for di in directions:
                new_row = row + di[0]
                new_col = col + di[1]
                if 0<=new_row<ROW and 0<=new_col<COL:
                    neightbors.append((new_row,new_col))
            return neightbors
        
        def DFS(row,col,nodes,visited):
            # when to stop
            if A[row][col]==1 and (row,col) not in visited:
                visited.add((row,col))
                nodes.add((row,col))
            else:
                return
            
            for coor in find_neighors(row,col):
                new_row,new_col = coor
                DFS(new_row,new_col,nodes,visited)

        objects = []
        visited = set()
        for r in range(ROW):
            for c in range(COL):
                if A[r][c]==1 and (r,c) not in visited:
                    nodes = set()
                    DFS(r,c,nodes,visited)
                    objects.append(nodes.copy())
        start,end = objects
        
        
        stack = collections.deque([(node,0) for node in start])
        end = set(end)
        visited = set(start)
        while stack:
            node, d = stack.popleft()
            
            if node in end:
                return d-1
                

            for node in find_neighors(*node):
                if node not in visited:
                    stack.append((node,d+1))
                    visited.add(node)

        