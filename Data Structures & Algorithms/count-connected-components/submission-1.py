class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {}

        for i in range(n):
            graph[i] = []
        
        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set() 
        
        def dfs(node):
            visited.add(node)

            for neighbour in graph[node]: 
                if neighbour not in visited: 
                    dfs(neighbour)
        

        component = 0 

        for node in range(n): 
            if node not in visited: 
                dfs(node)
                component += 1
        
        dfs(0)
        return component
            


# goal: return the number of connected components in the graph 

# build an adjacency list from edges 
# keep a visited set 
# loop through every node 0...n-1
# if a node has not been visited then run dfs/bfs from it
    # increment components 




# example 1: 
    # input --> n = 5, edges = [[0,1],[1,2],[3,4]]


    
    # if there is a cycle --> components = 1
    # might be excessive to do cycle detection for one edge case


 
    