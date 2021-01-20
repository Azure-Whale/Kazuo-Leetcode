class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        Brute-force
        Check number of those not in right order
        '''
        # cnt = 0
        # target_heights = sorted(heights)
        # for m,n in zip(heights,target_heights):
        #     if m!=n: cnt += 1
        """
        Counting Sort
        https://www.youtube.com/watch?v=7zuGmKfUt7s
        counting sort is kind of a algo using O(n) but can only address a small amount of data cuz it cannot be operated in-place.
        You may use counting sort to get correct list and then do a comparation
        """
        # create a copy to store the array in correct order
        sorted_heights = [0] * len(heights)
        # get freq from the arr
        freq_ = dict()
        for h in heights:
            freq_[h] = freq_.setdefault(h, 0) + 1
        # Key: do not sort these keys but iterate it from the min to max, space ← time
        previous = 0
        for h in range(min(heights), max(heights) + 1):
            freq_[h] = freq_.setdefault(h, 0) + previous
            previous = freq_[h]
        # Since we got the freq for range[min,max],if there is corresponding element in origin arr, then use dict to get the poi and update it in the meanwhile
        for h in heights:
            index = freq_[h] - 1
            freq_[h] -= 1
            sorted_heights[index] = h
        # Count the occurances which is not in right order for the origin arr
        return sum(m != n for m, n in zip(heights, sorted_heights))
