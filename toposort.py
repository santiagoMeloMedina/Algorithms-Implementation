from collections import deque

visited = [0]*len(G)
order = deque()

def dfs(n):
    global G, visited, order
    visited[n] = 1
    for m in G[n]:
        if visited[m] == 0:
            dfs(m)
    order.appendleft(n)

def toposort():
    global G, visited, order
    for n in range(len(G)):
        if visited[n] == 0:
            dfs(n)
    print(order)


# G = [[1,2], [2,3], [3,5], [4], [], [], [], [6]] // Directed Acyclic Graph
# toposort()
