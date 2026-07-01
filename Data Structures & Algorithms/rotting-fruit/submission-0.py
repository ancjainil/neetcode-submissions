class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh=0
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                elif grid[r][c]==2:
                    q.append((r,c))
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        time =0

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()

                for dr,dc in directions:
                    nr = r+dr
                    nc = c+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]==1 and (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
            time+=1
        return time if fresh==0 else -1



        