#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 2D-game.py
@Time    : 2/18/2021 4:27 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

"""
Question 1
We are designing a 2D game and we have a game map that we represent by an
integer matrix. For now, each cell can be a wall (denoted by -1) or a blank
space (0).
"""
board = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
start_point = [(3, 1), (5, 3), (5, 1), (6, 0), (6, 4), (0, 0), (2, 2),(2,4)]


def get_possible_steps(given_board, start_points):
    # check if the starting point available or not
    row, col = start_points
    ans = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    if not (0 <= row < len(given_board) and 0 <= col < len(given_board[0])) or given_board[row][col] == -1:
        return ans

    for di in directions:
        new_row = row + di[0]
        new_col = col + di[1]
        if (0 <= new_row < len(given_board) and 0 <= new_col < len(given_board[0])) and given_board[new_row][new_col] != -1:
            ans.append((new_row, new_col))

    return ans


for case in start_point:
    available_steps = get_possible_steps(board, case)
    print(available_steps)
