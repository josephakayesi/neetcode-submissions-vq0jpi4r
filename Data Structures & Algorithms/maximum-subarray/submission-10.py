class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums = [2,-3,4,-2,2,1,-1,4]

        THought process:
        - Two decisions -  discard left sub or continue with left sub to form right sub
                                
        """
        current_max = 0
        maxSub = nums[0]

        for num in nums:
            if current_max < 0:
                current_max = 0
            
            current_max += num
            maxSub = max(maxSub, current_max)
        return maxSub