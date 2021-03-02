from collections import deque
class Solution:
    
    def calculate(self, s: str) -> int:
        # double O(n) n is the length of the string
        stack = deque()
        res = 0
        number = 0
        sign = 1
        for char in s:
            if char == '+':
                res += number * sign
                number = 0
                sign = 1
            elif char =='-':
                res += number * sign
                number = 0
                sign = -1
            elif char =='(':
                stack.append(res)
                stack.append(sign)
                res = 0
                number = 0
                sign = 1
            elif char == ')':
                res += number * sign
                res *= stack.pop()
                res == stack.pop()
                sign = 1
                number = 0
            elif char.isdigit():
                number = (number * 10 )+ int(char)


        res += number*sign
        return res