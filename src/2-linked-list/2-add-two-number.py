# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        cur = ans
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val + carry
            carry = sum // 10
            newNode = ListNode(sum % 10)
            cur.next = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            cur = cur.next
        return ans.next
