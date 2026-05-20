class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def paths(row, col):
            # Base case 
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