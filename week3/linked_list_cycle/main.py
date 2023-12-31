from solution import Solution
from listnode import ListNode

sol = Solution()


if __name__ == '__main__':

    data0 = [3,2,0,-4]
    head0 = ListNode(data0[0])
    temp = head0
    for i in data0[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    head0.next.next.next.next = head0.next

    data1 = [1,2]
    head1 = ListNode(data1[0])
    temp = head1
    for i in data1[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    head1.next.next = head1

    data2 = [1]
    head2 = ListNode(data2[0])
    temp = head2
    for i in data2[1:]:
        temp.next = ListNode(i)
        temp = temp.next

    print(sol.hasCycle(head0))
    print(sol.hasCycle(head1))
    print(sol.hasCycle(head2))
