def flatlandSpaceStations(n, c):
    c.sort()
    print(c)    
    max_distance = max(c[0], n - 1 - c[-1])
    for i in range(1, len(c)):
        max_distance = max((c[i] - c[i-1]) // 2, max_distance)
    return max_distance
        
print(flatlandSpaceStations(5, [0, 4]))