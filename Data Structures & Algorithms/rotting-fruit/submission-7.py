from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        stack = deque()
        for i in range(ROWS):
            for j in range(COLS):
                cell = grid[i][j]
                if cell == 1:
                    fresh +=1
                if cell == 2:
                    stack.append((i,j))
        moves = [0,1,0,-1,0]
        minute = 0
        while fresh >0 and stack:
            for _ in range(len(stack)):
                r,c = stack.popleft()
                for i in range(4):
                    nr,nc = r+moves[i], c+moves[i+1]
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] ==1:
                        stack.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh-=1
            minute+=1
        return minute if fresh == 0 else -1