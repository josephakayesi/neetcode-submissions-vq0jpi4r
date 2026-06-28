class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set(nums)
        res = 0
        
        for num in elements:
            if (num - 1) in elements:
                continue
            
            longest = 0
            while num in elements:
                longest += 1
                num += 1
                
            res = max(res, longest)
        return res
            









