from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        dirs = [0,1,0,-1,-1,1,1,-1,0]
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        if ROWS==COLS==1:
            return 1
        start,end = -1,-2
        grid[0][0] = -1
        grid[ROWS-1][COLS-1] = -2
        stack1 = deque([(0,0)])
        stack2 = deque([(ROWS-1,COLS-1)])
        length = 2
        while stack1 and stack2:
            for _ in range(len(stack1)):
                r,c = stack1.popleft()
                for i in range(8):
                    nr,nc = r+dirs[i],c+dirs[i+1]
                    if 0<=nr<ROWS and 0<=nc<COLS:
                        if grid[nr][nc] == end:
                            return length
                        if grid[nr][nc] == 0:
                            grid[nr][nc] = start
                            stack1.append((nr,nc))
            length+=1
            start,end = end,start
            stack1,stack2 = stack2,stack1
        return -1