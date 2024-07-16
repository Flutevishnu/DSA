NF = float("inf")

graph = [[0, 1, 9]]


def bellman(n: int, edges: list[list[int]], s: int):
    dist = [INF] * n
    dist[s] = 0

    for i in range(n - 1):
        # relax
        for edge in edges:
            u, v, wt = edge
            x = dist[u] + wt
            if (dist[u] != INF) and x < dist[v]:
                dist[v] = x

    for edge in edges:
        u, v, wt = edge
        x = dist[u] + wt
        if (dist[u] != INF) and x < dist[v]:
            return [-1]

    return dist


print(bellman(2, graph, 0))