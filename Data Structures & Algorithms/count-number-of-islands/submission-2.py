class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def dfs(grid,sr,sc):
            nonlocal ROWS
            nonlocal COLS
            if 0<=sr<ROWS and 0<=sc<COLS and grid[sr][sc] == "1":
                grid[sr][sc] = 1
                dfs(grid,sr+1,sc)
                dfs(grid,sr,sc+1)
                dfs(grid,sr-1,sc)
                dfs(grid,sr,sc-1)
                return 1
            print('0')
            return 0
        for i in range(0,ROWS):
            for j in range(0,COLS):
                islands+=dfs(grid,i,j)
        return islands