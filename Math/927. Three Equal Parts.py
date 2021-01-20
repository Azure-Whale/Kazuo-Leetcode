#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : 927. Three Equal Parts.py
@Time    : 1/16/2021 6:30 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''


class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        # A = [0,0,..1,1,0..]
        # leading zero allowed
        """
        The key points:
        1. leading zero is nothing, ending zero has meaning. So, if we find the static part, it would be eaiser to find range of each part
        2. The last part can help use find the static part, as you don't need to consider leading zero of next part. Once we find static part, try to match previous elements
        3. overlap 0, if we find a 1, then try to match it with static part, if it does, directly go to next part.
        3. If there is an answer, it must satisfy some certain conditions. (number of ones)
        """
        # if cannot divided by 3, return [-1,-1]
        if A.count(1) % 3 != 0:
            return [-1, -1]
        if A.count(1) == 0:
            return [0, len(A) - 1]
        # get the correct number of ones that each part should have
        correct_ones = A.count(1) / 3

        # get the static part(removed leading zeros), use it for further processing
        static_part = []
        cnt = 0
        for i in A[::-1]:
            static_part.append(i)
            if i == 1:
                cnt += 1
                if cnt == correct_ones:
                    break
        static_part = static_part[::-1]

        i = 0
        option = []
        while i < (len(A) - len(static_part)):
            if A[i] == 0:
                i += 1
            elif A[i] == 1 and A[i:i + len(static_part)] == static_part:
                option.append(i)
                if len(option) == 2:
                    return [option[0] + len(static_part) - 1, option[1] + len(static_part)]
                i = i + len(static_part)
                continue
            else:
                return [-1, -1]
        return [-1, -1]

#    Verify method, time out
#         def remove_leading_zero(ele):
#             for i in range(len(ele)):
#                 if ele[i]!=0:
#                     return ele[i:]
#             return [0]

#         def check(i,j,A):
#             a = remove_leading_zero(A[:i+1])
#             b = remove_leading_zero(A[i+1:j])
#             c= remove_leading_zero(A[j:])
#             if a==b and b==c:
#                 return True
#             else:
#                 return False

#         print(A[:16],A[16:32],A[32:])
#         print(len(A))
#         num_of_1 = sum(A)
#         if num_of_1%3 != 0:
#             print('end1')
#             return [-1,-1]
#         part1_ = 0
#         for i in range(len(A)):
#             if A[i] == 1:
#                 part1_ += 1
#                 num_of_1 -= 1
#             if part1_*2>num_of_1:
#                 return [-1,-1]
#             if part1_*2==num_of_1:
#                 part2_ = 0
#                 part3_ = num_of_1
#                 for j in range(i+1, len(A)):
#                     if A[j] == 1:
#                         part2_ += 1
#                         part3_ -= 1
#                     if part2_==part3_:
#                         print(i,j)
#                         if check(i,j+1,A):
#                             print('end2')
#                             return [i,j+1]
#                     if part2_>part3_:
#                         print(i,j)
#                         print('end3')
#                         break
#         print('end3')
#         return [-1,-1]

