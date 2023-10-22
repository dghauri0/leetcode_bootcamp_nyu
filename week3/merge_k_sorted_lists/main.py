from typing import Optional, List
from solution import Solution
from listnode import ListNode

sol = Solution()


if __name__ == '__main__':

    data0 = [[1,4,5],[1,3,4],[2,6]]
    input_heads0 = []
    for j in range(len(data0)):
        head0 = ListNode(data0[j][0])
        temp = head0
        for i in data0[j][1:]:
            temp.next = ListNode(i)
            temp = temp.next
        input_heads0.append(head0)

    data1 = []
    head1 = ListNode()
    temp = head1
    for i in data1[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    data2 = [[]]
    head2 = ListNode(data2[0])
    temp = head2
    for i in data2[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    print(sol.mergeKLists(input_heads0))
    print(sol.mergeKLists(head1))
    print(sol.mergeKLists(head2))
