class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        
        visited = set()
        
        islands = 0
        def dfs(r,c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] != "1":
                return
            grid[r][c] = "0"
            
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
                
        
        for r in range(rows):
            
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visited:
                    
                    dfs(r,c)
                    islands += 1
        return islands
        
        
            
