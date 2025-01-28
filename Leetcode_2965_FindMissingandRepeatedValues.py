#2965 Find Missing and Repeated Values
def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    s = set()
    res = [0, 0]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] not in s:
                s.add(grid[i][j])
            else:
                res[0] = grid[i][j]
    n = len(grid)**2
    sum_n = n * (n+1)//2
    res[1] = sum_n - sum(list(s))
    return res
