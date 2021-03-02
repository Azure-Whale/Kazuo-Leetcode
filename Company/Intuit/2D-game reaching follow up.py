#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 2D-game reaching follow up.py
@Time    : 2/18/2021 4:47 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

"""
Given a board and an end position for the player, write a function to
determine if it is possible to travel from every open cell on the board to
the given end position.
"""
board1 = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
board2 = [
    [0, 0, 0, 0, -1],
    [0, -1, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [-1, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
    [0, -1, 0, 0, 0],
]
board3 = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, 0, 0, 0, -1, 0],
    [0, -1, -1, -1, -1, -1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]
board4 = [
    [0, 0, 0, 0, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, -1, -1, -1, 0],
    [0, 0, 0, 0, 0],
]
end1 = (1, 0)
end2 = (5, 0)


def solution(board, end_point):
    row, col = end_point
    # if endpoint is X, return false
    if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] == -1:
        return False
    count_walls = 0
    visited = set()
    # mark all walls as visited
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1:
                visited.add((i, j))

    visited.add(end_point)
    res = bfs(board, end_point, count_walls, visited.copy())
    print(res)


def bfs(board, start_point, count_walls, visited):
    if (len(visited)) == len(board) * len(board[0]):
        return True

    for step in get_possible_steps(board, start_point):

        if step not in visited:
            visited.add(step)
            res = bfs(board, step, count_walls, visited)
            if res:
                return True

    return False


def get_possible_steps(board, start_points):
    # check if the starting point available or not
    row, col = start_points
    ans = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] == -1:
        return ans

    for di in directions:
        new_row = row + di[0]
        new_col = col + di[1]
        if (0 <= new_row < len(board) and 0 <= new_col < len(board[0])) and board[new_row][new_col] != -1:
            ans.append((new_row, new_col))

    return ans


for board in [board1, board2, board3, board4]:
    for end_point in [end1, end2]:
        solution(board, end_point)
