class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        area =0
        
        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            visit.add((r,c))
            res =1
          
            while queue:
                row,col = queue.popleft()
                for dr, dc, in directions:
                    nr, nc = dr+row, dc+col
                    if (nr<0 or nr==ROWS or nc<0 or nc==COLS or grid[nr][nc]== 0 or (nr,nc) in visit):
                        continue
                    queue.append((nr,nc))
                    visit.add((nr,nc))
                    res+=1

            return res


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    area = max(area,bfs(r,c))    
        return area
        