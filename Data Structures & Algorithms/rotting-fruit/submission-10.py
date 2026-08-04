class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [0,1,0,-1,0]
        ticks = 0
        fresh = 0
        rottable = True
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh+=1
        while fresh>0:
            rottable = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for i in range(4):
                            nr,nc = r+moves[i], c+moves[i+1]
                            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                                grid[nr][nc] = 3
                                rottable = True
                                fresh-=1
            ticks+=1
            if not rottable:
                return -1
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

        return ticks