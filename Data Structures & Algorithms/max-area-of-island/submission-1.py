class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area=0

        def bfs(r,c):
            q= deque()
            q.append((r,c))
            visited.add((r,c))
            res=1


            while q:
                row, col = q.pop()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc

                    if r in range(ROWS) and c in range(COLS) and grid[r][c]==1 and((r,c)) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
                        res+=1
                
            return res





        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c]==1:
                    area = max(area, bfs(r,c))



        return area
        