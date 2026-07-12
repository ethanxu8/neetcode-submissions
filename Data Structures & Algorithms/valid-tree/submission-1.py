class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1: 
            return False 
        
        graph = defaultdict(list)

        # keep track of neighbours 
        for u, v in edges: 
            graph[u].append(v)
            graph[v].append(u)

        visited = set() 

        def dfs(node, parent):

            visited.add(node)

            for neighbour in graph[node]: 
                
                # case 1: neighbour is parent 
                if neighbour == parent: 
                    continue 
                
                # case 2: neighbour already visited 
                if neighbour in visited: 
                    return False 
                
                # case 3: unexplored neighbour 
                if not dfs(neighbour, node): 
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n 


        

        # keep a visited set() 
        # dfs(node, parent)






#  condition: has exactly n-1 edges 
    # if n != len(edges) - 1, return False 

# cycle detection 
    # dfs or bfs? 



# A graph is a valid tree if and only if it satisfies two conditions:

# It is connected (every node is reachable from every other node).
# It has no cycles.

# An equivalent fact that is extremely useful is:

# A graph with n nodes is a tree iff

# it has exactly n - 1 edges, and
# it is connected.
        
        