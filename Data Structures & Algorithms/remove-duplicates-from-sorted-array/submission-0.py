class Solution:
    """
    nums=[2,10,10,30,30,30]
             s  f  
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        sp, fp = 0, 1
        while fp < len(nums):
            if nums[sp] == nums[fp]:
                nums.pop(sp)
                continue

            sp += 1
            fp += 1
        return len(nums)


