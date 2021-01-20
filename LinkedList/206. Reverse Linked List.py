# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        '''Iterative'''
        new_head = None

        while head:  # 当前Node是否为空？
            temp = head.next  # 存储下一个Node的位置
            head.next = new_head  # 切断当前Node和下一个Node联系，并将当前Node指向自己前面的Node
            new_head = head  # 更新倒序LinkedList的head，即当前Node
            head = temp  # 进入到下一个原LinkedList的Node
        return new_head

    '''Recursive Method'''
    '''def __init__(self):
        self.reverse = ListNode(0)
        self.new_head = self.reverse

    def recursive(self,head):
        if head.next == None:
                self.reverse.next = ListNode(head.val)
                self.reverse = self.reverse.next
                return self.reverse

        res = self.recursive(head.next)
        res.next = ListNode(head.val)
        res = res.next
        return res


    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        self.recursive(head)
        return self.new_head.next'''




