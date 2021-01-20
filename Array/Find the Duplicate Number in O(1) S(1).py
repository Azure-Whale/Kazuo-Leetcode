class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # It is same with the question of finding the linked list cycle in same conditions
        # Using Floyid algo
        # make the list as a LL, it does do when it is in this case, refer the mind of question 142 of LL

        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


