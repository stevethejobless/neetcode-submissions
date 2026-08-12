from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid) , len(grid[0])
        moves = [0,1,0,-1,0]
        fresh = 0
        minutes = 0
        stack = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh+=1
                if grid[i][j] == 2:
                    stack.append((i,j))
        
        while fresh and stack:
            for _ in range(len(stack)):
                r,c = stack.popleft()
                for i in range(len(moves)-1):
                    nr,nc = r+moves[i], c+moves[i+1]
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        stack.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh-=1
            minutes+=1

        return -1 if fresh else minutes
        
