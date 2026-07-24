from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(grid,stack):
            nonlocal moves
            nonlocal ROWS
            nonlocal COLS
            while stack:
                r,c = stack.pop()
                grid[r][c] = 0
                for i,j in moves:
                    nr = r+i
                    nc = c+j
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == "1":
                        stack.append((nr,nc))
            
        for i in range(0, ROWS):
            for j in range(0,COLS):
                if grid[i][j] == "1":
                    islands+=1
                    stack = deque([(i,j)])
                    bfs(grid,stack)

        return islands