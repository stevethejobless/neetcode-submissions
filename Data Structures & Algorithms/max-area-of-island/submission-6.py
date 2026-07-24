class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(grid,r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return ( 1 + dfs(grid,r+1,c)
                + dfs(grid,r-1,c)
                + dfs(grid,r,c+1)
                + dfs(grid,r,c-1)                
            )


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(grid,i,j))
        
        return max_area