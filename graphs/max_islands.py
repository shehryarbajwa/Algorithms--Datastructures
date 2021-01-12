def max_islands(grid):
    max_island = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                max_island = max(max_island, visit(grid, row, col))
    return max_island

def visit(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
        return 0

    grid[row][col] = 'visited'

    u = visit(grid, row + 1, col)
    v = visit(grid, row - 1, col)
    w = visit(grid, row, col + 1)
    x = visit(grid, row, col - 1)

    return 1 + u + v + w + x