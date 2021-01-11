def number_islands(grid):
    num_islands = 0
    visited = [[False for col in row] for row in grid]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                visit(grid, row, col)
                num_islands += 1
    return num_islands

def visit(grid, row, col):

    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or visited[row][col] or grid[row][col] != '1':
        return

    visited([row][col]) = True
    
    visit(grid, row + 1, col)
    visit(grid, row - 1, col)
    visit(grid, row, col + 1)
    visit(grid, row, col - 1)


