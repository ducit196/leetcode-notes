from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        if root == None:
            return None
        q = deque()
        depth = -1
        ans = []
        q.append((root, 0))
        while q:
            node, currentDepth = q.popleft()
            #New level, add a new array
            if currentDepth > depth:
                ans.append([node.val])
                depth = currentDepth
            else:   #Same level, append to current path
                ans[-1].append(node.val)
            if node.left:
                q.append(node.left, currentDepth + 1)
            if node.right:
                q.append(node.right, currentDepth + 1)
        return ans
