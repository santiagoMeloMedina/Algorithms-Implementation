from queue import PriorityQueue
import math

def dijkstra(n):
    global G
    pq = PriorityQueue()
    dist = [math.inf]*len(G)
    pq.put((0,n))
    dist[n] = 0
    while not pq.empty():
        item = pq.get()
        for m in G[item[1]]:
            if dist[m[0]] > item[0]+m[1]:
                dist[m[0]] = item[0]+m[1]
                pq.put((item[0]+m[1], m[0]))
    print(dist)


# G = [[(2,6), (4,1)], [(2,2), (3,3), (4,6)], [(0,6), (1,2), (3,7)], [(1,3), (2,7), (4,5)], [(0,1), (1,6), (3,5)]]
# dijkstra(0)
