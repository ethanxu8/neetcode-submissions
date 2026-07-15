class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges) + 2)]

        def find(x): 
            if parent[x] != x: 
                parent[x] = find(parent[x])
            return parent[x]
        

        def union(a, b): 
            parent[find(a)] = find(b)


        for a, b in edges: 
            if find(a) == find(b): 
                return [a,b]
            union(a,b)






# goal: return an edge that can be removed so that 
    # graph is connected 
    # non-cyclical graph 


# we can do cycle detection and if there is a cycle, return last edge 
    # may be too excessive for this question? 
    # this would work for example 1 where we have an entire cycle 

# 



# example 1:
    # cyclical so remove the last edge 

# example 2: 
    # [4,5] is the only edge that can get to 5 so we cannot remove it 
    # there are two wasy to connect 134 so we remove the latest one which is [3,4]

        