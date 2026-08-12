class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if ROWS == COLS == 1 and (grid[0][0] == 2 or grid[0][0]==0):
            return 0

        moves = [0,1,0,-1,0]
        fresh = 0
        rot = True
        minutes = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh+=1
        
        while fresh and rot:
            rot=False
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 3:
                        grid[i][j] = 2
                        
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 2:
                        for k in range(len(moves)-1):
                            nr,nc = i+moves[k], j+ moves[k+1]
                            if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                                rot = True
                                grid[nr][nc] = 3
                                fresh -=1
            
            minutes+=1
        
        return -1 if fresh else minutes



