# https://leetcode.com/problems/combinations/

class Solution:
    """
    The target is to 
    """
    def __init__(self):
        self.ans = []
        self.target_length = None

    def combine(self, n: int, k: int) -> List[List[int]]:
        elements = list(range(1,n+1))
        self.target_length = k

        def find_ele(combination, index, elements,remaining):
            temp_combine = combination.copy()
            if not remaining:
                if len(temp_combine) == self.target_length:
                    self.ans.append(temp_combine)
                print(temp_combine)
                return
            remaining -= 1
            # actually, we can save some space using pop()
            for i in range(index+1,len(elements)-remaining):
                temp_combine.append(elements[i])
                find_ele(temp_combine, i, elements,remaining)
                temp_combine = combination.copy()
                
                
        remaining = k - 1
        for i in range(len(elements)-remaining):
            combination = [elements[i]]
            find_ele(combination, i, elements,remaining)
        
        return self.ans