class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        def dfs(i, j, visited): 

            visited.add((i, j))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for di, dj in directions: 
                ni, nj = i + di, j + dj

                # Check for index out of bounds 
                if ni < 0 or ni >= rows or nj < 0 or nj >= cols: 
                    continue 
                
                # check if cell was already visisted 
                if (ni, nj) in visited: 
                    continue

                # check for condition 
                if heights[ni][nj] < heights[i][j]: 
                    continue 
                
                dfs(ni, nj, visited)
        
        pacific = set()
        atlantic = set()

        # pacific covers top row and left col 
        # top row 
        for j in range(cols): 
            dfs(0, j, pacific)

        # left col
        for i in range(rows): 
            dfs(i, 0, pacific)

        # atlantic covers bottom row and right col
        # bottom row 
        for j in range(cols): 
            dfs(rows-1, j, atlantic)

        # right col
        for i in range(rows): 
            dfs(i, cols-1, atlantic)
        

        both = pacific & atlantic 
        return list(both) 







     
            # reaches pacific and atlantic, res.append(heights[i][j])
        
            # pacific 
            # [0][anything] or [anything][0]

            # atlantic 
            # [anything][len(grid)] or [len(grid[0])][anyting]
        

           




        # foundation: heights[i][j] >= heights[i+1][j] or heights[i][j+1]         