#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 1197. Minimum Knight Moves.py
@Time    : 12/2/2020 10:27 AM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        """
        每个落点都可以当成上一个落点的child,实际上那这就是一个有8个child都是又互相连接的Tree,但是有一些child有多个parent,所以必须切断这些联系,这里可以用一个set来记录已经visited过的child
        对于这道题来说我们不需要搜索无关的区域,所以设置了一个限制不用遍历不需要的child, 但是如果你要走 例如1,1必须跨界(4分界限)
        对于已经被放到stack中的child来说,它已经被遍历了,不需要在后续的搜索中重复加入到queue中
        这是一道经典的BFS问题 + 队列
        """
        target_x = abs(x)
        target_y = abs(y)
        visited = set()
        queue = deque()
        found = False
        queue.append((0, 0))
        cnt = 0
        temp = deque()

        def get_moves(x, y):
            return ((x + 2, y + 1), (x + 2, y - 1), (x - 2, y - 1), (x - 2, y + 1), (x + 1, y - 2), (x + 1, y + 2),
                    (x - 1, y - 2), (x - 1, y + 2))

        while queue:
            # get current node
            x, y = queue.popleft()
            # if not found, then add all its children to the queue
            if x == target_x and y == target_y:
                found = True
                return cnt
            else:
                moves = get_moves(x, y)
                for move in moves:
                    # when the move is not visited && satisfy the condition below → it avoid edge case, like (1,1), and no more searching in negative area
                    if move not in visited and (move[0] >= -1 and move[1] >= -1):
                        # when it is not visited, push it to the queue
                        visited.add(move)
                        temp.append(move)

            if not found and temp and not queue:
                queue = temp
                temp = deque()
                cnt += 1




