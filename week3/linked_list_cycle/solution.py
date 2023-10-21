# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from listnode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp0 = head.next
        temp1 = head
        if temp0 == None:
            return False
        while temp1 != None:
            if temp0.val == temp1.val:
                return True
            temp1 = temp1.next
        return False