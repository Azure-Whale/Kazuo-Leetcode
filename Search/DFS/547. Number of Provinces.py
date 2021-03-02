#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 547. Number of Provinces.py
@Time    : 1/31/2021 3:46 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''
# https://leetcode.com/problems/number-of-provinces/
"""There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c. 

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise. 

Return the total number of provinces.

 
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # O(n^2) The main idea is DFS, for each group, iterate all its nodes and add them into the visited. Once you find an unvisited node, there should be a new group.
        # isConnected[i][j] = 1 if the ith city and the jth city are directly connected
        def DFS(i):
            if i in viewed:
                return
            viewed.add(i)
            # find the node connected to it
            for j in range(n):
                # if the node is itself, ignore it
                if i == j:
                    continue
                # if there is, find more nodes
                if isConnected[i][j]:
                    DFS(j)

        ans = 0
        viewed = set()  # viewed set
        n = len(isConnected)
        for i in range(n):
            # if there is corresponing de
            if isConnected[i][i] and (i not in viewed):
                DFS(i)
                ans += 1
            else:
                continue
        return ans

