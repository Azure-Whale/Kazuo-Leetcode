#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 79. Word Search.py
@Time    : 2/13/2021 4:16 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''
#https://leetcode.com/problems/word-search/
"""
The key point here is that:
1. Using backtracking to search the word
2. How to record those visited to prevent re-visit? dict or a trick below(Space(1))
3. If there is a need to track the path, pass a copy of a list to record walked path




"""


class Solution:

    def __init__(self):
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        m = len(board)
        n = len(board[0])

        for row in range(m):

            for col in range(n):

                if board[row][col] == word[0]:
                    ans = self.backtracking_dfs(board, row, col, word, [])
                    if ans:
                        print(ans)
                        return ans
        return ans

    def backtracking_dfs(self, board, row, col, remaining_words, records):
        m = len(board)
        n = len(board[0])
        # if the node cannot provide needed char
        if len(remaining_words) == 0:
            return records

        out_of_index = (row < 0 or col < 0 or row >= m or col >= n)
        if out_of_index or remaining_words[0] != board[row][col]:
            return False

        # prevent the dfs to visit those visited, can be replace by dict
        temp = board[row][col]
        board[row][col] = '!visited'
        records.append((row, col))  # to record the path how dfs finds the target
        # CAA
        # AAA
        # BCD
        for row_offeset, col_offset in self.directions:

            temp = self.backtracking_dfs(board, row + row_offeset, col + col_offset, remaining_words[1:],
                                         records.copy())
            if temp:
                return temp
        # needs to be converted back
        board[row][col] = temp
        return False
