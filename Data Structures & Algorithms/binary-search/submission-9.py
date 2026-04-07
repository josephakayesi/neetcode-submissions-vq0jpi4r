class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Intuition
        - We know the array is sorted and hence we can use binary search on it. 
        - Keep two pointers; low and high
        - At the start; low points to first element and high points to last element
        - Find the mid point and check if the mid == target. 
        - If the target is lesser than the mid then we move our high to the mid and check the left half of the array
        - Otherwise we move low to mid and check the right half. 
        - Keep doing this until we find the target or low overalps with high and at that point return -1 to indicate the target was not found
        """

        low = 0
        high = len(nums) - 1 

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid 

            if nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
        
        return -1
