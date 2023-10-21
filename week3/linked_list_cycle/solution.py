# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from listnode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        for i in head:
            for j in head:
                if i != j:
                    if i.next == j.next:
                        return True
        return False