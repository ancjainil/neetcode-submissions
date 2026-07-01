class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        vis=set()
        islands=0
       
       
        if not grid:
            return 0
        
        
        def bfs(r,c):
            q= deque()
            q.append((r,c))
            vis.add((r,c))
            directions =[(1,0), (-1,0), (0,1), (0,-1)]
            
            while q:
                
                row, col = q.popleft()
                for dr,dc in directions:
                    
                    r= row+dr
                    c= col+dc
                    if r in range(rows) and c in range(cols) and grid[r][c]=='1' and (r,c) not in vis:
                        q.append((r,c))
                      
                        vis.add((r,c))
                    
            
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in vis:
                    bfs(r,c)
                    islands+=1
        
        return islands
        