class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition:
        - Thinking of the array as a circular buffer helps form a better intuition
        - Rotated sorted array forms a circular buffer
        - We find which halves are sorted
        - Within each half:
            - Is the target in that half or does it wrap around to the other half
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m 

            # left sorted portion

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1