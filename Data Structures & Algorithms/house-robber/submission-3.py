class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Intuition:
        - Two choices:
            - Rob a house
            - Or not rob a house
        - If you decide to rob a house you must skip the adjacent house. 
        - However robber must ensure maximum amount 
        - Recurrence: rob(i) + rob(i + 2) 
        - Maximum of current house robbed
        - If out of boundes: -> 0
        """

        memo = {}

        def rob(house):
            # Base case: No more houses to rob
            if house >= len(nums):
                return 0
            
            if house in memo:
                return memo[house]
            
            memo[house] = max(nums[house] + rob(house + 2), rob(house + 1))

            return memo[house]
        
        return rob(0)