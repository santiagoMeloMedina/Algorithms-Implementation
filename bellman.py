import math

def bellman(n):
    global G
    dist = [math.inf]*len(G)
    dist[n] = 0
    for nn in range(len(G)-1):
        for m in range(len(G)):
            for s in G[m]:
                dist[s[0]] = min(dist[s[0]], dist[m]+s[1])
    print(dist)

# G = [[(2,6), (4,1)], [(2,2), (3,3), (4,6)], [(0,6), (1,2), (3,7)], [(1,3), (2,7), (4,5)], [(0,1), (1,6), (3,5)]]
# bellman(0)
