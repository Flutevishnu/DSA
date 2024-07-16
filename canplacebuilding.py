def can_place_buildings(grid, buildings):
    count = 0
    n = len(grid)
    i = 0

    while i < n:
        if grid[i] == 0 and (i == 0 or grid[i-1] == 0) and (i == n-1 or grid[i+1] == 0):
            count += 1
            grid[i] = 1  
            i += 1  
        i += 1

    return count >= buildings

