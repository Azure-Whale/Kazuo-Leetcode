class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # method 1
        # use math + binary search
        # convert the coordinate of matrix into a whole array
        m = len(matrix)
        if m == 0:
            # avoid []
            return False
        n = len(matrix[0])

        # binary search
        left, right = 0, m * n - 1
        while left <= right:
            pivot_idx = (left + right) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_idx - 1
                else:
                    left = pivot_idx + 1
        return False

        # Firstly, you search the column using a search algo you like,
        # you may use same to search the row then
        # The main idea here is to narrow the range where the target lied

        # method 2, search row and search col

        if not matrix or not matrix[0]:
            return False

        def binary_search_row(nums):
            """
            Using binary search to ensure the range is different from typical binary search
            The left or right will be replace by mid instead of mid +- 1.
            Also, you shall deal with the edge case when target is more than or less than the max or min
            """
            left = 0
            right = len(nums) - 1

            if target <= nums[left][0]:
                return left
            elif target >= nums[right][0]:
                return right

            while left <= right:
                mid = (right + left) // 2
                if mid == left:
                    return left
                if nums[mid][0] < target:
                    left = mid
                elif nums[mid][0] == target:
                    return mid
                elif nums[mid][0] > target:
                    right = mid

        def binary_search_col(nums):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return None

        row = binary_search_row(matrix)
        col = binary_search_col(matrix[row])

        if col != None:
            return True
        else:
            return False