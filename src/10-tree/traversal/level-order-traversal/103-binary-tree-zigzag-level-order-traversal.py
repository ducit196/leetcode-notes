from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        ans = []
        q.append((root, 0))
        while q:
            curNode, curDepth = q.popleft()
            #logic here
            if curDepth >= len(ans):
                ans.append([curNode.val])
            elif curDepth % 2 == 0:
                ans[curDepth].append(curNode.val)
            else:
                ans[curDepth].insert(0, curNode.val)
            if curNode.left:
                q.append((curNode.left, curDepth + 1))
            if curNode.right:
                q.append((curNode.right, curDepth + 1))
        return ans
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().zigzagLevelOrder(root))