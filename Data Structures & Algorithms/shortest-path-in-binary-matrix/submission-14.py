from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def mat_print():
            for row in grid:
                print(row)
            print()
        if grid[0][0] == 1: 
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        stack = deque([(0,0,1)])
        dirs = [(0,1),(0,-1),(1,0),(-1,0),
            (1,1),(1,-1),(-1,1),(-1,-1)]
        
        print(1)
        mat_print()

        while stack:
            for _ in range(len(stack)):
                r,c,l = stack.popleft()
                print(l)
                mat_print()
                if r == ROWS-1 and c == COLS-1:
                    return l
                for x,y in dirs:
                    nr = r+x
                    nc = c+y
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc]==0:
                        grid[nr][nc] = -1
                        stack.append((nr,nc,l+1))
        return -1