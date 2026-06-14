class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Goal
        - You are starting at cell `grid[0][0]` and you need to reach cell `grid[m-1][n-1]`
        - You are allowed to move in two directions: `down` or `left`
        - From our starting point; how many number of ways can we take to reach our destination
        
        Thought process
        - At each cell we have two decisions to make: `down` or `left`
        - Our stopping condition is when we reach `grid[m-1][n-1]`
        - Start traversing from starting point.
        - Take both decisions (down or left) and check if we are within bounds before proceeding. 
        - If within bounds continue from that cell moving in either directions. 
        - If we reach out destination then increment our valid pathways.
        - Keep doing this until we have either reached our final destintation or
            our directions takes us out of bounds 

        dfs(0, 0):
            dfs(1, 0):
                dfs(2, 0)
                dfs(1, 1)
            dfs(0, 1)
                dfs(1, 1)
                dfs(0, 2)
        """

        memo = {}

        def paths(row, col):
            # Base case - Check if position out of bounds
            if row == m or col == n:
                return 0 

            if row == m - 1 and col == n - 1:
                return 1

            # Memo check 
            if (row, col) in memo:
                return memo[(row,col)]

            memo[(row, col)] = paths(row, col + 1) + paths(row + 1, col)

            return memo[(row, col)]

        return paths(0, 0)
        