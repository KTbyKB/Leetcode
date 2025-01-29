#1971 Find-if-path-exists-in-graph

def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adj_list = {v : [] for v in range(n)}
    for v1, v2 in edges:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    visited = [False]*n
    stack = []
    stack.append(source)

    while stack:
        ele = stack.pop(0)           
        if ele == destination:
            return True
        for i in adj_list[ele]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
            
    return False
