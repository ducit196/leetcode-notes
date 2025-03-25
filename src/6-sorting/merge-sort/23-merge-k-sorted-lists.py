# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge sort idea
        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

        def mergeSort(nums):
            if len(nums) <= 1:  # base case
                return nums[0]
            left = mergeSort(nums[0: len(nums) // 2])
            right = mergeSort(nums[len(nums) // 2:len(nums)])
            return mergeTwoLists(left, right)

        return mergeSort(lists)

node1 = ListNode(1, ListNode(4, ListNode(5)))
node2 = ListNode(1, ListNode(3, ListNode(4)))
node3 = ListNode(2, ListNode(6))
lists = [node1, node2, node3]
print(Solution().mergeKLists(lists))