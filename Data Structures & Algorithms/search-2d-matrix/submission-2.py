# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         """
#         - first start by check the values at the beginning of and end of each row. 
#         - if target value is withing the row then iterate through that row. 

#         matrix = [[1,2,4,8],
#                   [10,11,12,13],
#                   [14,20,30,40]]

#         target = 15

#         """

#         R, C = len(matrix), len(matrix[0])

#         for r in range(R):
#             if target >= matrix[r][0] and target <= matrix[r][C - 1]:
#                 # find element within the row
#                 for c in range(C):
#                     if target == matrix[r][c]:
#                         return True

#         return False
            
           
        
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        left, right = 0, R * C - 1

        while left <= right:
            mid = (left + right) // 2
            r = mid // C
            c = mid % C

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
