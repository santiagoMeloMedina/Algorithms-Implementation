
def preorder(n):
    global G, order
    order.append(n)
    for m in G[n]:
        preorder(m)

def inorder(n):
    global G, order
    if len(G[n]): inorder(G[n][0])
    order.append(n)
    for m in range(1, len(G[n])):
        inorder(G[n][m])

def posorder(n):
    global G, order
    for m in G[n]:
        posorder(m)
    order.append(n)


# G = [[1,2], [3,4], [], [], []] # Tree (Undirected Acyclic Graph)
# order = []
# inorder(0)
# print(order)
