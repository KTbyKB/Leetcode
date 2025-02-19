def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(grid, i, j):           
        if i < 0 or i > nr-1 or j < 0 or j > nc-1 or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
        dfs(grid, i-1, j)
        dfs(grid, i+1, j)

    nr = len(grid)
    nc = len(grid[0])
    c = 0
    for i in range(nr):
        for j in range(nc):
            if grid[i][j] == '1':
                c += 1
                dfs(grid, i, j)
    return c
