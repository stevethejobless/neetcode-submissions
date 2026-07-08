class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid,i,j,visited):
            if 0<=i<lr and 0<=j<lc and (i,j) not in visited and grid[i][j] == "1" :
                visited.add((i,j))
                print(visited)
                dfs(grid,i+1,j,visited)
                dfs(grid,i-1,j,visited)
                dfs(grid,i,j+1,visited)
                dfs(grid,i,j-1,visited)
        lr,lc = len(grid), len(grid[0])
        islands = 0
        visited = set()
        for i in range(0,lr):
            for j in range(0,lc):
                if (i,j) not in visited and grid[i][j] == "1":
                    islands+=1
                    dfs(grid,i,j,visited)
        return islands
        
