# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        # Set method, time O(1);space O(n)
        # visited = set()
        # while head:
        #     if head in visited:
        #         return head
        #     visited.add(head)
        #     head = head.next
        # return None

        # Floyd's Tortoise and Hare
        # Keep two priciples, there are two pointers, one's speed is 1 unit, and the other one is 2 units. It's granteed that they will meet in the cycle(F+a) if there is a cycle
        # If they start from start and intersection, it's garanteeed that they will meet at the entrance of the cycle
        # more details please check https://leetcode.com/problems/linked-list-cycle-ii/solution/

        if not head:
            return None

        def get_intersection(head):
            print('Phase1, check the existence of phase1')
            ptr1 = head
            ptr2 = head
            # if there is no cycle, one pointer would exceed evetually
            while ptr2 is not None and ptr2.next is not None:
                ptr2 = ptr2.next.next
                ptr1 = ptr1.next
                # the speed of ptr2 is double of ptr1
                if ptr2 == ptr1:
                    return ptr2
                # if these two pointers converge, then there must be a loop, then break
            return None

        # Phase 2, there is a loop
        # ptr1 start from the head, while the ptr2 start from the intersection
        print('Phase2, check the existence of phase2')
        ptr1 = head
        ptr2 = get_intersection(head)
        if ptr2 is None:
            return None

        while ptr1 != ptr2:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        return ptr1

