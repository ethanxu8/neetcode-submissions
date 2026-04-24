"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node): 
            if node in old_to_new: 
                return old_to_new[node]
            else: 
                copy = Node(node.val)
                old_to_new[node] = copy 
            
            for neighbor in node.neighbors: 
                copy.neighbors.append(dfs(neighbor))
        
            return copy 

        if not node: 
            return None 
        
        return dfs(node)
            
        

        
        



       



        # REACTO 
        # goal: return a deep copy of the graph 

        # Example1: len(adjList) = 3 nodes 
            # list in list contains neighbours, index is node.val

        # Example2: empty node with no neighbours 

        # Example 3: empty graph --> edge case 


        # Approach: 
        # define bfs or dfs
        # think dfs would work better here 



        # append neighbours 












        