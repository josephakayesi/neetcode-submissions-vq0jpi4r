class Solution:
    """
    Intuition:
    - Keep a low and a high pointer
    - The low points to the lower value in the range and the high points to the high pointer in the range
    - While the low and high are still in range; check for the mid value. 
    - If the mid is equal to the target; then return that value
    - If the target value < mid then reduce the range
    - If the target value > mid then increase the range
    """

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                r = mid - 1
                continue 
            
            if target > nums[mid]:
                l = mid + 1
                continue 
        
        return -1