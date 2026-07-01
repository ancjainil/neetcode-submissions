''' O(logN) '''

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        islands =0
        visited = set()




        def bfs(r,c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            directions = [(0,1), (1,0), (0,-1), (-1,0)]

            while q:
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if (nr < 0 or nr >= ROWS or nc< 0 or nc>= COLS or (nr,nc) in visited or grid[nr][nc]=='0'):
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))




        for r in range(ROWS):
            for c in range(COLS):

                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1

        return islands



        
        