def numIslands(grid):
    # dfs from every possible location
    # dfw up down left right
    # have end conditions check for out of bounds, or if val == 0:
    # end search for given thing.
    # track visited cords.
    # visited.add()
    # dfs
    # visited.remove()

    # go from top left to bottom right. each start will yield either a final island OR none
    # as you go, mark all visited so they are not included.
    ROWS, COLS = len(grid), len(grid[0])

    visited = set()
    total = 0

    def dfs(cords, visited):
        x, y = cords

        if cords in visited:
            return

        if x < 0 or x > ROWS - 1:
            return

        if y < 0 or y > COLS - 1:
            return
        
        visited.add(cords)
        
        if grid[x][y] == "0":
            return # Stop search, but do NOT remove visited!

        up = (x, y - 1)
        right = (x + 1, y)
        down = (x, y + 1)
        left = (x - 1, y)

        dfs(up, visited)

        dfs(right, visited)

        dfs(down, visited)

        dfs(left, visited)
    
    for x in range(ROWS):
        for y in range(COLS):
            if grid[x][y] == "0" or (x, y) in visited:
                continue

            cords = (x, y)
            dfs(cords, visited)
            total += 1
    
    return total

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numIslands(grid))