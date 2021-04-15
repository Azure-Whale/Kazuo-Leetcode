import math
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # all elements are positive integers, so the subarray is meant to be larger as it grows
        # use two pointer to find the ans
        # Key: when extending the subarray, the extra number of subarraries ending with nums[i] is (end - start + 1)
        if not nums or k<=1:
            return 0
        start = ans = 0
        curr_prod = 1
        for end, val in enumerate(nums):
            curr_prod *= nums[end]
            if curr_prod < k:
                pass
            else:
                while curr_prod>=k: # if nums[i]>k, start will be next index and ans will add 0
                    curr_prod /= nums[start]
                    start += 1
            ans += (end - start + 1) 
        return ans
            