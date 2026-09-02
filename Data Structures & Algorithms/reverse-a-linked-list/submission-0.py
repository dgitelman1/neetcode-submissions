# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need to make it such that for each node, the next value points at the one previous
        prev = None
        while head:
            # store next node
            temp = head.next
            # set current node to be previous
            head.next = prev
            # set previous node to be current and move up
            prev = head
            head = temp
        return prev