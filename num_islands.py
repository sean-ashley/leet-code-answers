class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols = len(grid),len(grid[0])
        
        visited = set()
        
        islands = 0
        def bfs(r,c):
            
            queue = deque()
            queue.appendleft((r,c))

            while queue:
                row,col = queue.pop()

                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                
                for dr,dc in directions:
                    if  (row+dr) in range(rows) and (col+dc) in range(cols) and grid[row+dr][col+dc] == "1" and ((row+dr),(col+dc)) not in visited:
                        queue.appendleft((row+dr,col+dc))
                        visited.add((row + dr,col + dc))

                        
                
        
        for r in range(rows):
            
            for c in range(cols):
                
                if grid[r][c] == "1" and (r,c) not in visited:
                    
                    bfs(r,c)
                    islands += 1
        return islands
        
        
            
