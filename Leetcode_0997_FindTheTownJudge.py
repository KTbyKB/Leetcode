#997 Find The Town Judge

def findJudge(self, n: int, trust: List[List[int]]) -> int:
    degree = [0]*(n+1)
    for v1, v2 in trust:
        degree[v1] -= 1
        degree[v2] += 1
        
    for i in range(1,n+1):
        if degree[i] == n-1:
            return i
    return -1
