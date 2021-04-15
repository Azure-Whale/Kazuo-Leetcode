class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        #we create a 2D matrix presenting the longest Fobi seq ending with i,j
        # say there is a sequence A[i], A[j] , A[k], it is one of Fibonacci seq
        # longest[i][j] should be 2 in this case, if we are able to find k in the given seq, then and longest[j][k] should be longest[i][j] + 1, of course, k should be larger than the j in this case
        # try to find this parttern from the beginning of the seq, then we will get the longgest Fibo finally, it is similar to the consecutive incresing seq
        longest = collections.defaultdict(lambda:2)
        value_look_up = {value:idx for idx,value in enumerate(arr)}
        ans = 0
        if len(arr)<3:
            return ans
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                k = arr[i] + arr[j]
                if k in value_look_up and k>j:
                    longest[(j,value_look_up[k])] = max(longest[(i,j)] + 1,longest[(j,value_look_up[k])])
                    ans = max(longest[(j,value_look_up[k])],ans)
        print(longest)
        return ans
        