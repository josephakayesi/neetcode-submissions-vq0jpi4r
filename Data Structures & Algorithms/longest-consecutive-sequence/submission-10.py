class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Keep all elements in a dictionary 
        Iterate elements. 
        Check each element if its a start of a sequence. 
            - I need to check if the element - 1 exists in the dictionary
            - If it doesn't start sequence
                - Now calculte the longest consecutive sequence
            - If it does then skip (because its not sequence)

Time: O(n)
Space: O(n)
        """
        elems = {}
        res = 0

        for n in nums:
            if n in elems:
                continue 
            
            elems[n] = True 

        for n in nums:
            if n - 1 in elems:
                continue 
            
            curr_max = 0 

            curr = n
            while curr in elems:
                curr_max += 1
                curr += 1 

            res = max(res, curr_max)

        return res