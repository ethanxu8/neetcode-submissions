# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')): 
            if not node: 
                return True
            val = node.val
            if node.val <= lower or node.val >= upper: 
                return False 
            # look at left subtree
            if not helper(node.left, lower, val): 
                return False
            # look at right subtree 
            if not helper(node.right, val, upper): 
                return False
            return True
        
        return helper(root)
   
        
    
        # if not root return False 


        # self.val > self.left and self.val < self.right
        