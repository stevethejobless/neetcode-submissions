class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        stack = []
        max_area = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    area = 1
                    stack.append((i,j))
                    while stack:
                        r,c = stack.pop()
                        for x,y in moves:
                            nr = r+x
                            nc = c+y
                            if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                                stack.append((nr,nc))
                                grid[nr][nc] = 0
                                area+=1
                    max_area = area if area > max_area else max_area
        
        return max_area

