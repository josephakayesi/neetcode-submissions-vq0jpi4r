# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         """
#         - Iterate nums
#         - Find subarray for each num 
#         - Find maximum
#         - Return maximum


#         Solution - 2
#         - Iterate nums
#         - Keep running max
#         - Update max_subarray 
#         - If current_max < 0:
#             current_max = 0 
#         - Return max_subarray
#         """

#         # max_subarray = 0 

#         # for i in range(len(nums)):
#         #     for j in range(i, len(nums)):
#         #         current_max = sum(nums[i:j+1])

#         #         max_subarray = max(max_subarray, current_max)

#         # return max_subarray

#         current_max = 0
#         max_subarray = nums[0]

#         for i in range(len(nums)):
#             current_max = max(nums[i], current_max + nums[i])
#             max_subarray = max(max_subarray, current_max)

#         return max_subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Intution:
        - Keep a pointer moving from left -> right 
        - Add the current sum.
        - We want to maximize the the sum hence two choices. 
        - If the curr_sum < 0 then we can reset our sum 
        - Otherwise keep going. 
        - Keep a running max_sum 
        """

        res = nums[0]
        curr_sum = 0

        for num in nums:
            curr_sum += num  
            res = max(res, curr_sum)

            if curr_sum < 0:
                curr_sum = 0

        return res




