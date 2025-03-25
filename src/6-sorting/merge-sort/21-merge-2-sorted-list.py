from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        ans = ListNode()
        curAns = ans
        while cur1 or cur2:
            val1 = cur1.val if cur1 else 101
            val2 = cur2.val if cur2 else 101
            if val1 < val2:
                newNode = ListNode(val1)
                cur1 = cur1.next
            else:
                newNode = ListNode(val2)
                cur2 = cur2.next
            curAns.next = newNode
            curAns = curAns.next
        return ans.next