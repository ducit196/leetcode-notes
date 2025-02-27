from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode()
        curAns = ans
        cur = head
        while cur:
            if cur.val != val:
                newNode = ListNode(cur.val)
                curAns.next = newNode
                curAns = curAns.next
            cur = cur.next
        return ans.next

head = ListNode(1, ListNode(2, ListNode(2, ListNode(4))))
print(Solution().removeElements(head, 2))