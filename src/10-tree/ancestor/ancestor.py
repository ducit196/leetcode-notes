



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left != None and right != None: return root
        if left != None: return left
        return right
p = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
q = TreeNode(1, TreeNode(0), TreeNode(8))
root = TreeNode(3, p, q)
print(Solution().lowestCommonAncestor(root, p, q))