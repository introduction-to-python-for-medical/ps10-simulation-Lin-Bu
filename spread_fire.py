import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    update_grid = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            if j == grid_size-1 and i == grid_size-1 and grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i][j-1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2
            elif j == grid_size-1 and grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2
            elif i == grid_size-1 and grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2
            elif grid[i][j] == 1:
                neighbors = [grid[i-1][j],grid[i+1][j],grid[i][j-1],grid[i][j+1]]
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid
