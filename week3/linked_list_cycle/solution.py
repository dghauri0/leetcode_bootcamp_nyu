# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional
from listnode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Maintain a list of visited nodes.
        visited = []

        # Traverse list checking if already visited and adding to visited.
        temp = head
        while temp is not None:
            if temp in visited:
                return True
            visited.append(temp)
            temp = temp.next

        return False
