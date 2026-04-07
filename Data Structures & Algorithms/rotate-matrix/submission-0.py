class Solution:
    """
    For 2x2 matrix 
    (0,0) -> (0,1)
    (0,1) -> (1,1)
    (1,1) -> (1,0)
    (1,0) -> (0,1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])

        left, right = 0, R -1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right 

                #  save top left 
                topLeft = matrix[top][left + i]

                # move bottom left into top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # move bottom right into bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # move top right into bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # mave top left into top right
                matrix[top + i][right] = topLeft
            
            right -= 1
            left += 1

        
        