from collections import deque

def tarjan():
    global G, depth, low, parents, art, brid, bcc, bcctmp, added
    depth = [-1]*len(G)
    low = [-1]*len(G)
    parents = [-1]*len(G)
    art, brid, bcc = set(), set(), []
    bcctmp = deque()
    added = {}
    for u in range(len(G)):
        if depth[u] == -1:
            depth[u] = low[u] = 0
            dfs(u)
        if len(bcctmp):
            b = bcctmp.pop()
            tmp = []
            while len(bcctmp):
                tmp.append(b)
                b = bcctmp.pop()
            tmp.append(b)
            bcc.append(tmp)
    return art, brid, bcc

def dfs(u):
    global G, depth, low, parents, art, brid, bcc, bcctmp, added
    children = 0
    for v in G[u]:
        if depth[v] == -1:
            children += 1
            depth[v] = low[v] = depth[u]+1
            parents[v] = u
            if tuple(sorted([u,v])) not in added:
                bcctmp.append(tuple(sorted([u,v])))
                added[tuple(sorted([u,v]))] = 1
            dfs(v)
            low[u] = min(low[u], low[v])
            if (parents[u] == -1 and children > 1) or (parents[u] != -1 and low[v]>=depth[u]):
                art.add(u)
                b = bcctmp.pop()
                tmp = []
                while b != tuple(sorted([u,v])):
                    tmp.append(b)
                    b = bcctmp.pop()
                tmp.append(b)
                bcc.append(tmp)

            if low[v]>depth[u]:
                brid.add((u,v))

        elif parents[u] != v:
            low[u] = min(low[u], depth[v])
            if tuple(sorted([u,v])) not in added:
                bcctmp.append(tuple(sorted([u,v])))
                added[tuple(sorted([u,v]))] = 1

#G = [[1,6], [0,2,3,5], [1,3,4], [1,2,4], [2,3], [1,6,7,8], [0,5], [5,8], [5,7,9], [8], [11], [10]]
print(tarjan())
