class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Intuition:
        - Keep a hash map of the the num and its diff
        - Whilst iterating through the nums we check the diff; if the diff already exists in the hash; there there is a corresponding number
          that sums up to the target
        - After iterating and there is no two integers; return false

        nums = [3, 4, 5, 6]
        target = 7 

        kv = {
            3: 0,

        }

        nums = [4, 5, 6]
        target = 10

        kv = {
            4: 0,
            5: 1,

            
        }

      nums = [5, 5]
        target = 10

        kv = {
            5: 0
            
            
        }

        """

        kv = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in kv:
                return [kv[diff], i]
            
            kv[nums[i]] = i
        
