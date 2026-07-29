from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1
        stack = deque([(0,0)])
        dirs = [0,1,0,-1,-1,1,1,-1,0]
        length = 1
        while stack:
            for _ in range(len(stack)):
                r,c = stack.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                for i in range(len(dirs)-1):
                    nr,nc = r+dirs[i], c+dirs[i+1]
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] != 1:
                        grid[nr][nc] = 1
                        stack.append((nr,nc))
            length+=1
        return -1

