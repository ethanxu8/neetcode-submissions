# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tree_vals = []

        def traverse(node):
            nonlocal tree_vals

            if not node: 
                return 

            traverse(node.left)
            tree_vals.append(node.val) 
            traverse(node.right)
        
    
        traverse(root)

        return tree_vals[k-1]
    



        # all elements in the left subtree < root 
        # all elements in the right subtree > root 

        # if we know root_int = k smallest int of root 
            # if root_int == k: return root.val 
            # if root_int < k: go into right subtree 
            # if root_int > k: go into left subtree
        
            # if we can keep track of int for each node then 
                # if root.val == k, return root.val 



        