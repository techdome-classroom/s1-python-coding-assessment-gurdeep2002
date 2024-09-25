class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        
         if not grid:
            return 0  # Edge case: empty grid
        
    
    # Dimensions of the grid
            rows, cols = len(grid), len(grid[0])
    
    def dfs(r, c):
        # If out of bounds or at water, stop the DFS
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
            return
        # Mark the landmass as visited by changing 'L' to 'W' or any other marker
            grid[r][c] = 'W'
        # Explore the four adjacent directions
            dfs(r+1, c)  # Down
            dfs(r-1, c)  # Up
            dfs(r, c+1)  # Right
            dfs(r, c-1)  # Left

    # Island count
        island_count = 0
    
    # Iterate over every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found an unvisited landmass
                    island_count += 1  # This is a new island
                    dfs(r, c)  # Perform DFS to mark the entire island
    
        return island_count

# Test cases

grid1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]

grid2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]

print(num_islands(grid1))  # Output: 1
print(num_islands(grid2))  # Output: 3

    
                    
        return 0
