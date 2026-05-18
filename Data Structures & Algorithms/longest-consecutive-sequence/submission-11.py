class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        nums = [2,20,4,10,3,4,5]
        nums_set = (2, 20, 5, 10, 3, 5)
        longest = 4
        
        length = 1

        """
        nums_set = set(nums)
        longest = 0

        for nums in nums_set:
            if (nums - 1) in nums_set:
                continue 
            
            length = 1
            while (nums + length) in nums_set:
                length += 1
            longest = max(longest, length)
        
        return longest