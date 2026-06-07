class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Thought process
        - Use a variation of kadanes algorithm
        - First start iterating through the nums list
        - Keep a running current_max
        - When the current_max goes below 0; then we need to reset our max_subarray
        - If the current `i` > the max_subarray then we need to reset current_max and start finding the current_max from that positon
        - Do this until we have completed the iteration
        - Return our max_subarray

        nums = [-1]

        current_max = 0
        max_list = -1
        """


        current_max = 0
        max_list = nums[0]

        for num in nums:
            if current_max < 0:
                current_max = 0 
           
            current_max += num
           
            max_list = max(max_list, current_max)

        return max_list
