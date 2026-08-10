from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        moves = [0,1,0,-1,0]
        stack = deque()
        visit = set()
        max_area = 0

        def bfs(r,c):
            stack.append((r,c))
            visit.add((r,c))
            print(visit)
            area=0
            while stack:
                r,c = stack.popleft()
                for i in range(len(moves)-1):
                    nr,nc = r+moves[i],c+moves[i+1]
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1 and (nr,nc) not in visit:
                        visit.add((nr,nc))
                        stack.append((nr,nc))
                area+=1
                
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    max_area = max(max_area,bfs(r,c))
        
        return max_area
