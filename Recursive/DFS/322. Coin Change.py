#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 322. Coin Change.py
@Time    : 1/22/2021 8:28 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Greedy? No, you may get an answer but not the correct one as it requires the minimal one.

        def DFS(coins, amount, current_amount, num_coins):
            option = None
            if current_amount == amount:
                return num_coins
            elif current_amount > amount:
                return float('inf')
            else:
                for coin in coins:
                    temp = DFS(coins, amount, current_amount + coin, num_coins + 1)
                    if not option:
                        option = temp
                    else:
                        option = temp if temp < option else option
                return option

        res = DFS(coins, amount, 0, 0)

        return res if res > 0 else -1
