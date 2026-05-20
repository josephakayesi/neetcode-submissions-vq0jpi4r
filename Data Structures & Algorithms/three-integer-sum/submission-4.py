class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Assumptions:
        - There is guaranteed to be at least one triplet
        - Triplets sum to zero

        Intuition:
        - First sort the nums list
        - Iterate through the nums list
        - For each iteration do a two sum:
        - Use two pointers. j and k. j starts at j + 1 and k starts at len(nums) - 1
        - Find the triplet totla
        - If total == 0 -> add triplet
        - If total < 0 -> j += 1
        - If total > 0 -> k -= 1

                         i  l     r
        nums = [-4, -1, -1, 0, 1, 2]

        triplets = [[-1, -1, 2], [-1, 0, 1]]

        i
        l
        r

        """

        nums.sort() 
        triplets = []

        for i, a in enumerate(nums):
            # Avoid duplicate at i 
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplets.append([nums[i], nums[l], nums[r]])

                    l += 1
                    # Avoid duplicate in two sum window
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return triplets


