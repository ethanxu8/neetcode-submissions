# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # handles when lca == p or lca == q
        if root == p or root == q: 
            return root 

        # both smaller so only check left subtree
        if p.val < root.val and q.val < root.val: 
            return self.lowestCommonAncestor(root.left, p, q)

        # both larger so only check right subtree
        if p.val > root.val and q.val > root.val: 
            return self.lowestCommonAncestor(root.right, p, q)
    
        # p and q not in same subtree so return root
        return root         