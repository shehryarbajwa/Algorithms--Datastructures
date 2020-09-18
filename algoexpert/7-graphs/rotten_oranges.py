class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        visited = [[False for col in rows] for rows in grid]
        rows = len(grid)
        cols = len(grid[0])
        
        queue = []
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append([row, col, 0])
                    visited[row][col] = True
        
        minutes = 0
        while queue:
            row, col, minutes = queue.pop(0)
            neighbours = self.get_unvisited_neighbours(row, col, grid, visited)
            for neighbour in neighbours:
                row_n = neighbour[0]
                col_n = neighbour[1]
                
                if grid[row_n][col_n] == 1 and not visited[row_n][col_n]:
                    queue.append([row_n, col_n, minutes + 1])
                    visited[row_n][col_n] = True
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    return -1
        return minutes
    
    def get_unvisited_neighbours(self, row, col, grid, visited):
        unvisited_neighbours = []
	
        if row > 0 and not visited[row - 1][col]:
            unvisited_neighbours.append([row - 1, col])
        if row < len(grid) - 1 and not visited[row + 1][col]:
            unvisited_neighbours.append([row + 1, col])
        if col < len(grid[0]) - 1 and not visited[row][col + 1]:
            unvisited_neighbours.append([row, col + 1])
        if col > 0 and not visited[row][col - 1]:
            unvisited_neighbours.append([row, col - 1])
        return unvisited_neighbours
                    
                
            
        