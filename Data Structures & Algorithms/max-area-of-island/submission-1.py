class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        areas = [0]
        moves = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(grid,r,c,area):
            grid[r][c] = 0
            area = 0
            for i,j in moves:
                nr=r+i
                nc=c+j
                if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 1:
                    area+=dfs(grid,nr,nc,0)
            area +=1
            return area

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    areas.append(dfs(grid,i,j,0))
        
        return max(areas)