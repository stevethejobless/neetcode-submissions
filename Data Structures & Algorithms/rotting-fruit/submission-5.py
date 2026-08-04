from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        if ROWS==COLS==1:
            return -1 if grid[0][0] == 1 else 0
            
        stack = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    print((i,j))
                    stack.append((i,j))
        if not stack:
            for i in range(ROWS):
                for j in range(COLS):
                    if grid[i][j] == 1:
                        return -1
            return 0

        moves = [0,1,0,-1,0]
        minute = -1
        while stack:
            for _ in range(len(stack)):
                r,c = stack.popleft()
                for i in range(4):
                    nr, nc = r+moves[i], c+moves[i+1]
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        stack.append((nr,nc))
                        grid[nr][nc] = 2
            minute+=1
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1
        return minute
        