import math

def warshall():
    global G
    for s in range(len(G)):
        for n in range(len(G)):
            for m in range(len(G)):
                G[n][m] = min(G[n][m], G[n][s]+G[s][m])
    print(*G, sep="\n")

# nl = math.inf
# G = [
#     [0, nl, 6, nl, 1],
#     [nl, 0, 2, 3, 6],
#     [6, 2, 0, 7, nl],
#     [nl, 3, 7, 0, 5],
#     [1, 6, nl, 5, 0],
#     ]
# warshall()
