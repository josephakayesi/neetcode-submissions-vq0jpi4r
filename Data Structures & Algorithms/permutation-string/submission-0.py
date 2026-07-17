class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Thought process
        - Iterate through s2 using the sliding window. 
        - At each window; take the subsequence and sort it. 
        - Check the sorted value with sorted(s1)
        - Keep doing this while sliding window in bounds

        s1 = "abc"
        
        s2 = "lecabee"
                l
                  r

        sub = "cab"
        s1_sorted = "abc"
        """

        if len(s2) < len(s1):
            return False

        l, r = 0, len(s1) - 1

        while r < len(s2):
            sub = s2[l:r + 1]

            if sorted(sub) == sorted(s1):
                return True 
            
            l += 1
            r += 1
        
        return False

        