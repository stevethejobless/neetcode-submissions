class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [0,1,0,-1,0]
        visit = set()
        area = 0
        def dfs(r,c,grid,visit):
            if r in range(0,ROWS) and c in range(0,COLS) and \
                (r,c) not in visit and grid[r][c] == 1:
                    visit.add((r,c))
                    count = 1
                    for i in range(len(moves)-1):
                        count+=dfs(r+moves[i], c+moves[i+1],grid,visit)
                    return count
            return 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    area = max(area,dfs(r,c,grid,visit))
        
        return area