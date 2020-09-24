from collections import deque

def tarjan():
    global G, depth, low, parents, visited, scc, scctmp, num_components
    depth = [-1]*len(G)
    low = [-1]*len(G)
    visited = [0]*len(G)
    scc, scctmp = [], deque()
    num_components = 0
    for u in range(len(G)):
        if depth[u] == -1:
            dfs(u)
    return scc

def dfs(u):
    global G, depth, low, parents, visited, scc, scctmp, num_components
    depth[u] = low[u] = num_components
    num_components += 1
    visited[u] = 1
    scctmp.append(u)
    for v in G[u]:
        if depth[v] == -1:
            dfs(v)
            low[u] = min(low[u], low[v])
        elif visited[v]:
            low[u] = min(low[u], depth[v])
    if (low[u]==depth[u]):
        s = scctmp.pop()
        tmp = []
        while s != u:
            tmp.append(s)
            s = scctmp.pop()
        tmp.append(s)
        scc.append(tmp)

G = [[2,3],[0],[1],[4],[]]
print(tarjan())
