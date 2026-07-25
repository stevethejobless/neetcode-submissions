from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque([(0,0)])
        visit = set([(0,0)])
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        length = 0
        while queue:
            length+=1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if r == ROWS -1 and c == COLS-1:
                    return length
                for x,y in dirs:
                    nr = r+x
                    nc = c+y
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in visit and grid[nr][nc] == 0:
                        visit.add((nr,nc))
                        queue.append((nr,nc))
        return -1
