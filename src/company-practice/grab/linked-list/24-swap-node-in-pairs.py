from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prevNode = dummy
        while head and head.next:
            firstNode = head
            secondNode = head.next
            prevNode.next = secondNode
            

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(Solution().swapPairs(head))
