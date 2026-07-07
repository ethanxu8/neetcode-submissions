class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()

        # add the treasure chests to a queue 
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 0: 
                    q.append((r, c))
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q: 
            r, c = q.popleft()    

            for dr, dc in directions: 
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols: 
                    continue 

                if grid[nr][nc] != 2147483647: 
                    continue 
                
                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))

        

        # add up 0's to a queue 

        # then grid[nr][nc] = gird[r][c] + 1
        # then add grid[nr][nc] to the queue

        