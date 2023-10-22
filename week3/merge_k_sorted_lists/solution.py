# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List
from listnode import ListNode


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list_1 = lists[i]
                if (i + 1) < len(lists):
                    list_2 = lists[i + 1]
                else:
                    list_2 = None
                merged_list.append((self.mergeLinkedList(list_1, list_2)))

            lists = merged_list
        return lists[0]

    def mergeLinkedList(self, list_1, list_2):
        temp = ListNode()
        tail = temp

        while list_1 and list_2:
            if list_1.val < list_2.val:
                tail.next = list_1
                list_1 = list_1.next
            else:
                tail.next = list_2
                list_2 = list_2.next
            tail = tail.next
        if list_1:
            tail.next = list_1
        if list_2:
            tail.next = list_2
        return temp.next
