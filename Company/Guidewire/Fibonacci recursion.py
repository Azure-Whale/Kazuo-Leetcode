class Solution:
    def fib(self, n: int) -> int:
        # num[i] + num[I+1] = nums[i+2]
        if n== 0:
            return 0
        if n == 1:
            return 1
        

        
        
        def recursion(a,b,cnt,N):
            if cnt == N:
                return a+b
            cnt += 1
            return recursion(b,a + b,cnt,N)
        return recursion(0,1,2,n)
        

        # the best method is iteration method as the time complexity is O(1)