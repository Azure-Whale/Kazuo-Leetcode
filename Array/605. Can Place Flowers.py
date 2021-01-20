#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 605. Can Place Flowers.py
@Time    : 11/18/2020 10:02 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    '''
    return True if n(the number of the plants you want to flower) <= maximum planted positions, otherwise return false
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N  = 0
        if len(flowerbed)==1:
            if flowerbed==[0]:
                return n<=1
            else:
                return n==0
        for i in range(0, len(flowerbed)):
            # if the place is empty
            if flowerbed[i] == 0:
                if i==0 and flowerbed[i+1]==0:
                    flowerbed[i] = 1
                    N += 1
                    continue
                if i==len(flowerbed) - 1 and flowerbed[i-1]==0:
                    flowerbed[i] = 1
                    N += 1
                    continue
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    N += 1

        return n<=N