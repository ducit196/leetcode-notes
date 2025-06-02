# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nums = []

        cur = head
        while cur:
            nums.append(cur.val)
            cur = cur.next
        print(nums)
        nums[k - 1], nums[-k] = nums[-k], nums[k - 1]
        print(nums)

        ans = ListNode()
        cur = ans
        for i in range(len(nums)):
            newNode = ListNode(nums[i])
            cur.next = newNode
            cur = cur.next
        return ans.next
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().swapNodes(head, 2))