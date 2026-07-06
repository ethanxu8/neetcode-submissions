class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = []

        def dfs(r, c): 

            if r < 0 or r >= rows or c < 0 or c >= cols: 
                return 0 
            
            if grid[r][c] == 0: 
                return 0 
            
            if (r, c) in visited: 
                return 0 
            
            visited.append((r, c))

            area = 1

            area += dfs(r+1, c)
            area += dfs(r-1, c)
            area += dfs(r, c+1)
            area += dfs(r, c-1)

            return area
        
        max_area = 0 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r, c) not in visited: 
                    max_area = max(max_area, dfs(r, c))
        
        return max_area



            # if out of bounds, return 0 

            # if grid[r][c] == 0, return 0 

            # if (r,c) in visited return 0 

            # visited.add((r, c))

            # area = 1 

            # area += dfs(r+1, c), area += dfs(r-1, c), area += dfs(r, c+1), area += dfs(r, c-1)
    


        # outer loop 

            # max_area = max(max_area, dfs(r, c))


        




            # if node.val == 0 immediately stop 
            # if node.val == 1 continue 
        
            # have a path to make sure you do not check visited nodes
    
        # return max_area




# dfs that explores all possible combinations 

# have a max_area that updates 


        