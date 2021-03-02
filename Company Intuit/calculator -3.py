from collections import deque
class Solution:
    
    var_map = {'a':4,'b':65}

    def calculate(self, s: str) -> int:
        # double O(n) n is the length of the string
        # Space Complexity, it should be O(n) as I used a stack to
        var_map = {'a':4,'b':65}
        not_know_var = {}
        stack = deque()
        res = 0
        number = 0
        sign = 1
        for char in s:
            if char.isalpha():
                if char in var_map.keys():
                    res += var_map[char] * sign
                else:
                    not_know_var[char] = not_know_var.setdefault(char,0) + sign

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
        ans = ''
        for var,count in not_know_var.items():
            if count == 1:
                count = ''
            if count == -1:
                count = '-'
            ans += f'{count}{var}'
        print(res)
        if res==0:
            res = ''
        elif res>0:
            res = '+'+str(res)
        elif res<0:
            res = str(res)
        ans += res
        return ans


a = Solution().calculate('(d-6)+5-c')
print(a)