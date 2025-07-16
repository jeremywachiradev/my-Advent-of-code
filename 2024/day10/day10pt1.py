input_grid = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip().split()

# Convert input to a 2D grid of integers
grid = []
for row in input_grid:
    grid.append([int(char) for char in row])

def dfs(matrix, row, col, current_height, visit, end_points):
    ROWS, COLS = len(matrix), len(matrix[0])
    
    # Check if out of bounds or already visited
    if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit:
        return
    
    # Check if the current cell has the expected height
    if matrix[row][col] != current_height:
        return

    # Add current position to visit set
    visit.add((row, col))
    
    # If we've reached height 9, add this position to end_points
    if current_height == 9:
        end_points.add((row, col))
        visit.remove((row, col))
        return
    
    # Explore all four directions, but only to cells with height = current_height + 1
    next_height = current_height + 1
    dfs(matrix, row+1, col, next_height, visit, end_points)
    dfs(matrix, row-1, col, next_height, visit, end_points)
    dfs(matrix, row, col+1, next_height, visit, end_points)
    dfs(matrix, row, col-1, next_height, visit, end_points)
    
    # Backtrack
    visit.remove((row, col))

results = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:  # Find all trailheads (height 0)
            end_points = set()  # Set to store unique positions with height 9
            dfs(grid, row, col, 0, set(), end_points)
            results.append(len(end_points))  # Count unique 9-height positions

print(results)  # This should output [5, 6, 5, 3, 1, 3, 5, 3, 5]
print(f"Sum of scores: {sum(results)}")  # Should be 36 for this example

"""
            tunatumia end_points ju tunacount only unique paths e.g. below
Consider a simple grid:
```
01
19
```
From the '0', we can reach the '9' via two different paths:
- 0→1→9 (going right then down)
- 0→1→9 (going down then right)
but the problem wants us to count this as 1 unique '9' cell that can be reached.
So the output should actually be 1 not 2 paths
"""