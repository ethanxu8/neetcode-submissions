# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, depth): 
            if not node: 
                return result 
            
            if depth == len(result): 
                result.append(node.val)
            
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)
        
        dfs(root, 0)
        return result


# REACTO 

# EXAMPLE 1: 
    # from root, return node.right 

# EXAMPLE 2: 
    # from root 
    # node.right 
    # node.right on left side 
    # node.right on left side 

    # start from root
    # check if node.left has a node.right, if yes use node.right 
    # if no, use node.left 
    # if no, use node.left

# Approach: 

# if not root, return result 
# if root.left and root.right, result.add(root.right)
# if not root.left and root.right, result.add(root.right)

# if root.left and not root.right, result.add(root.left)
