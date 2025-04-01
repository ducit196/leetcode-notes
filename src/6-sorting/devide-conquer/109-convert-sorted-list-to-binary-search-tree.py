from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:


        def midOfLinkedList(head):
            slow = head
            fast = head.next.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow


        def merge(head):
            if head == None:
                return None
            if head.next == None:
                return TreeNode(head.val)
            mid = midOfLinkedList(head)
            root = TreeNode(mid.next.val)
            right = mid.next.next
            mid.next = None
            left = head
            root.left = merge(left)
            root.right = merge(right)
            return root
        return merge(head)
head = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
print(Solution().sortedListToBST(head))