class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(nums: List[int]) -> int:
            memo = {}

            def steal(house):
                if house >= len(nums):
                    return 0
                
                if house in memo:
                    return memo[house]

                memo[house] = max(
                    nums[house] + steal(house + 2),
                    steal(house + 1)
                )

                return memo[house]

            return steal(0)
        
        return max(rob_linear(nums[:len(nums)-1]), rob_linear(nums[1:]))