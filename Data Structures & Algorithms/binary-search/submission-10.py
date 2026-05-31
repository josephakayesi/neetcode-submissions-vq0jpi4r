class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Assumptions
        - Search space is ordered. 
        - Only valid numbers are in search space

        Thought process
        - Use three pointers: left, mid, right
        - For every iteration: find the mid. 
        - If mid == target -> return index
        - If target > mid -> left = mid + 1
        - If target < mid -> right = mid - 1
        - If no value is found then return -1

                         m
        nums = [-1,0,3,5,9,12]
                       l    r
        target = 9
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2 # floor

            if nums[m] == target:
                return m
            
            if target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        