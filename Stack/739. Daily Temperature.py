from collections import deque
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = deque()
        stack.append((float('inf'),None))
        ans = [0]* len(T)
        for i in range(len(T)-1,-1,-1):
            # the curr is larger than the top layer, remove those smaller than it, if there is tie, we don't need those rank behind so we remove it as well
            while T[i]>=stack[-1][0]:
                stack.pop()
            if T[i]<stack[-1][0]:
                # if no othe element is larger than current, than only inf is larger than it and set 0 to it
                if stack[-1][0] == float('inf'):
                    stack.append((T[i],i))
                    continue
                # if at least found one element is larger than the curr, then the element must stay at the top of the stack. return the poi of the top layer of the stack - curr poi
                ans[i] = stack[-1][1] - i
                stack.append((T[i],i))
        return ans
