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

        Input: nums = [2,9,8,3,6]
                       0,1,2,3,4

        Output: 15

        memo = {
        (0, 3): 8,
        (2, 3): 8,
        (0, 4): 11
        (1, 4): 12
        (2, 4): 9
        (3, 4): 3
        
        }
        n = 5

        - rob(0, 3) -> 8:
            - 2 + rob(3, 3), 0 -> 2
                - 
            - rob(2, 3) -> 8:
                - 8 + rob(4, 3), 0: -> 8
                    - rob(4, 3) -> 0
                - rob(3, 3) -> 0


        - rob(0, 4): -> 12
            - 2 + rob(2, 4): -> 11
                - rob(2, 4): -> 9

            - rob(1, 4): -> 12
                - 9 + rob(3, 4): -> 3
                    - rob(3, 4): -> 3
                        - 3 + rob(5, 4), 0: -> 3
                        - rob(4, 4) -> 0

                - rob(2, 4) -> 9:
                    - 9 + rob(4, 4), 0: -> 9
                    - rob(3, 4): -> 3




        """

        memo = {}
        n = len(nums)

        if len(nums) == 1:
            return nums[0]

        def rob(house, last):
            # Base case: No more houses to rob
            if house >= last:
                return 0
            
            if (house, last) in memo:
                return memo[(house, last)]
            
            memo[(house, last)] = max(nums[house] + rob(house + 2, last), rob(house + 1, last))

            return memo[(house, last)]
        
        return max(rob(0, n - 1), rob(1, n))



