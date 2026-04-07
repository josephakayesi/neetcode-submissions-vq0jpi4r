class Solution:
    """
    start at the first cell [0, 0]
    at each cell check to see if the cell forms an island. 
    i.e iterate in all directions until the the island ends. 
        - keep track of all seen cells whilst check for islands

        grid = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]

grid = [

    [0, 1, 0],
    [0, 1, 1],
    [0, 1, 1]

]

  seen = {
    (1, 0),
    (1, 2)
  }

  res = 1
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0 
        R, C = len(grid), len(grid[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        seen = {}


        def dfs(r, c):
            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c

                # Its out of bounds
                if new_r < 0 or new_r >= R or new_c < 0 or new_c >= C:
                    continue

                # Its land; skip
                if grid[new_r][new_c] == "0":
                    continue 
                
                # Its water; continue building island
                if (new_r, new_c) not in seen:
                    seen[(new_r, new_c)] = True
                    dfs(new_r, new_c)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in seen:
                    res += 1
                    seen[(r, c)] = True

                    dfs(r, c)

        return res

        