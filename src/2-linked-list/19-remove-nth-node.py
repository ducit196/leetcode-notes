from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        # find total node
        total = 0
        curNode = head
        while curNode:
            curNode = curNode.next
            total += 1
        print(total)
        travel = total - n

        curNode = dummy
        while travel > 0:
            curNode = curNode.next
            travel -= 1
        curNode.next = curNode.next.next
        return dummy.next
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
head = ListNode(1)
print(Solution().removeNthFromEnd(head, 1))