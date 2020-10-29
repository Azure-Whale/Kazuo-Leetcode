#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 121. Best Time to Buy and Sell Stock.py
@Time    : 10/23/2020 11:39 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

"""
Refer to the max Subarray problem
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cur_profit = 0
        max_profit = 0
        low = 0
        high = 1
        if len(prices) <= 1:
            return 0
        else:
            while high < len(prices):
                if prices[high] < prices[low]:
                    low = high
                cur_profit = prices[high] - prices[low]
                if cur_profit > max_profit:
                    max_profit = cur_profit
                high += 1
        return max_profit

