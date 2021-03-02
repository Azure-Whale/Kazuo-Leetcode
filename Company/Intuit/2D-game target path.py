#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 2D-game target path.py
@Time    : 2/18/2021 10:02 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

board = [
    [1, 0, 0, 0, 0],
    [0, -1, -1, 0, 0],
    [0, -1, 0, 1, 0],
    [-1, 0, 0, 0, 0],
    [0, 1, -1, 0, 0],
    [0, 0, 0, 0, 0],
]

cnt = 0

def solution(board, start_point, end_point):
    global cnt
    row, col = end_point
    # if the endpoint is unavailable
    if not (0 <= row < len(board) and 0 <= col < len(board[0])) or board[row][col] == -1:
        return False
    get_treasure = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                cnt += 1
    res = DFS(board, start_point, end_point, get_treasure)
    return res


def DFS(board, start_point, end_point, get_treasure = False, curr_cnt =0):
    global cnt
    steps = get_possible_steps(board, start_point)
    # if get all T
    if curr_cnt == cnt:
        print('got it')
        get_treasure = True
    # if get all T and reached the endpoint, return True
    if get_treasure and start_point == end_point:
        return True
    if start_point == end_point:
        print(curr_cnt)
        print('reach the endpoint')
    row, col = start_point
    # if it is a T, curr cnt += 1
    if board[row][col] == 1:
        curr_cnt += 1
    board[row][col] = -1
    for s in steps:
        res = DFS(board, s, end_point, get_treasure,curr_cnt)
        if res:
            return True
    return False


def get_possible_steps(board, start_points):
    # check if the starting point available or not
    row, col = start_points
    ans = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    if not (0 <= row < len(board) and 0 <= col < len(board[0])):
        return ans

    for di in directions:
        new_row = row + di[0]
        new_col = col + di[1]
        if (0 <= new_row < len(board) and 0 <= new_col < len(board[0])) and board[new_row][new_col] != -1:
            ans.append((new_row, new_col))

    return ans

print(solution(board, (5,2),(2,0)))