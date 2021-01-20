
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Remain + LL waited to be reversed + Remain
        # when iterate:
        # Remain Part, just remain, LL part do a reversed as usual
        # Connect them
        # Make sure you return the correct head of the whole LL
        # if not left remain part, return end of LL
        # if have left remain part, return origin head of the whole LL
        ans = head # get head of the LL
        if hea d= =None: # if head is None
            return None
        cnt =0
        prev = None
        left = start = end = right = None
        while head:
            curr = head.val
            if cnt == m - 2:
                left = head
            if cnt == n:
                right = head
            if cnt == m - 1:
                start = head
            if cnt == n - 1:
                end = head
            if cnt >= m - 1 and cnt <= n - 1:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            else:
                head = head.next

            cnt += 1
        start.next = right
        if left:
            left.next = end
        else:
            ans = end
        return ans

#         while head:
#             if cnt == m-2:
#                 left = head
#             if cnt==n:
#                 right = head
#             if cnt==m-1:
#                 start = head
#             if cnt==n-1:
#                 end = head
#             cnt += 1
#             head = head.next

#         cnt = 0

#         last = right
#         head = ans
#         while head:
#             if m-1<=cnt<=n-1:
#                 next_node = head.next
#                 head.next = last
#                 last = head
#                 head = next_node
#             else:
#                 head=head.next
#             cnt += 1
#         if left:
#             end.next = left
#         return ans
