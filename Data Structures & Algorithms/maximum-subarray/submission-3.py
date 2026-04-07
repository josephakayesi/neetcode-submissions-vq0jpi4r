class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        nums = [2,-3,4,-2,2,1,-1,4]
        current_sum = 8
        max_so_far = 8

        Intuition
        - initialize a max_so_far and current_sum
        - Set max_so_far and current_sum to first elements of nums
        - Iterate from second element onwards
        - Keep a running current_sum;
        - Update max_so_far with current sum if it is greater than
        - Return the max_so_far 
        - 
        """ 

        max_so_far = nums[0]
        current_sum = 0

        for num in nums:

            # If current_sum < 0; then we ignore the previous elements as we have crossed to a better maximum
            if current_sum < 0:
                current_sum = 0

            current_sum += num
            max_so_far = max(max_so_far, current_sum)


        return max_so_far
