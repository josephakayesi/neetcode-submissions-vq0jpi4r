class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Thought process
            - Keep left, right, top and bottom markers on your matrix
            - Go from topLeft cell towards the right until you meet a wall;
            - Go downwards and keep going until you meet a wall
            - Go left and keep going until you meet a wall;
            - Go up until you meet a wall or the cell has alread been seen then go right

        - The trend is that you go in the following directions right -> down -> left -> up 
        - Keep a seen list or dict and before you move in any direction; check if you have already seen that cell 
            or it is a wall and keep going in that direction. This willl run m * n time and m*n space. 
        - Im sure there is a possibility where we do not use any extra space. WIll come back to it

        """

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res