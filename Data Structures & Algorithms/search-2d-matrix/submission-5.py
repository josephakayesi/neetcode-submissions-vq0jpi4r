class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Intuition
        - The intution here is that the matrix is sorted in an ascending order. 
        - Since the question requires a log(m * n) solution; we can use a binary search
        - We keep two pointers low and high
        - low starts at 0 and high starts at the last index. 
        - We ran a binary search on the matrix; 
        - When we find the mid point we translate the value to the corresponding matrix cell.
        - Similarly if we need to check in the right half or the left half; then we need to move the pointer to correspond mid + 1 or mid - 1 cell translation
       
        low = 0
        high = len(grid) * len(grid[0]) - 1 # 11

        rows = 3
        cols = 4

        0 - 3 => r = 0
        4 - 7 => r = 1
        8 - 11 => r = 2

        while low <= high:
            mid = (low + high) // 2 # 5 => matrix[1][1]

            mid_row = mid // cols => 5 // 4 => 1
            mid_col = mid // row => 5 // 3 => 1

            if grid[mid_row][mid_col] == target:
                return target
            
            if target < grid[mid_row][mid_col]:
                high = mid - 1
            else:
                low = mid + 1
            
        """

        R, C = len(matrix), len(matrix[0])
        low, high = 0, (R * C) - 1

        while low <= high:
            mid = (low + high) // 2 
            row = mid // C
            col = mid % C

            if target == matrix[row][col]:
                return True

            if target < matrix[row][col]:
                high = mid - 1
            else:
                low = mid + 1

        return False
