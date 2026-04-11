class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Intuition
        - For a single int:
            - Find the number of 1's by finding bin of integer and counting 1's
        
        - DO this for each int
        """

        res = [] 

        for i in range(n + 1):
            res.append(bin(i).count('1'))
        
        return res
        