import heapq

INF = float('inf')

graph = [
    [[1, 4], [2, 4]],
    [[0, 4, 2, 2]],
    [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
    [[2, 3], [5, 2]],
    [[2, 1], [5, 3]],
    [[2, 6], [3, 2], [4, 3]],
]

def dijkstra(n, graph, s):
    pq = []
    dist = [INF]*n
    
    dist[s] = 0
    heapq.heappush(pq, (0, s))

    while len(pq) != 0:
        distance, node = heapq.heappop(pq)
        for edge in graph[node]:
            edgenode = edge[0]
            edgedist = edge[1]

            x = distance+edgedist
            if (x<dist[edgenode]):
                dist[edgenode] = x
                heapq.heappush(pq, (x, edgenode))
    return dist


print(dijkstra(len(graph), graph, 0))