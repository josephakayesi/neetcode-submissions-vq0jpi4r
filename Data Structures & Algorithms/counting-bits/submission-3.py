# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         """
#         Intuition
#         - For a single int:
#             - Find the number of 1's by finding bin of integer and counting 1's
        
#         - DO this for each int
#         """



#         res = [] 

#         for i in range(n + 1):
#             res.append(bin(i).count('1'))
        
#         return res
        

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Intuition (Alternative)
        - For a each `i` in `n`:
            - Use the & operator to check if least significant bit is a 1
            - Increment count if it is. 
            - Right shift bits and repeat until i is 0
        
        - DO this for each int
        """

        res = [0] * (n + 1)

        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        
        return res
        