#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 66. Plus One.py
@Time    : 10/24/2020 10:51 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    '''
    Turn list into number
    transfer number res into list of int again
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        total = 0
        for i,v in enumerate(digits[::-1]):
            total += v*(10**i)
        return [int(v) for v in str(total+1)]
