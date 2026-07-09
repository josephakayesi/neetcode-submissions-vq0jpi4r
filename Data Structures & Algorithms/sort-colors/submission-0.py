class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = w = 0
        while s < len(nums):
            if nums[s] == 0:
                nums[s], nums[w] = nums[w], nums[s]
                s += 1
                w += 1
                continue
            s += 1
            
        s = w = len(nums) - 1
        while s >= 0:
            if nums[s] == 2:
                nums[s], nums[w] = nums[w], nums[s]
                s -= 1
                w -= 1
                continue
            s -= 1
        
        return nums
        