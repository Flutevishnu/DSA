'''Given a cost matrix cost[][] and a position (M, N) in cost[][], write a function that returns cost of minimum cost path to reach (M, N) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. The total cost of a path to reach (M, N) is the sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), and (i+1, j+1) can be traversed. '''

R = 3
C = 3


def minCost(cost, m, n):
    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = cost[0][0]

    
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]

   
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]

   
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]

    return tc[m][n]


cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(minCost(cost, 2, 2))