class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        THought process
        - For this problem we first need sort the elements in the nums list
        - Iterate through each num and then find the corresponding pair that makes our 3 sum
        - For the first loop we pick a number; say x.
        - Now we need to find two other numbers within the remiander of the nums list that make up y and z
        - x + y + z == 0
        - The seccond loop within the first loop will run a two operation to find the the other triplets. 
        - Now since the list is sorted; we can start our inner loop interation from opposite ends of that window. 
        - We update depending on if 3um > target or 3sum < target. 
        - If a triplet is found that add to res. 
        - Return result at the end. 
        - We can use a set to avoid duplicates.

        nums = [-4, -1, -1, 0, 1, 2]
                            i  l  r
        i = 0
        l = 1
        r = 5

        res = { (-1, -1, 2), (-1,  0, 1) }
        """

        nums.sort() 
        n = len(nums)
        res = set()

        # Last two elements will be part of last two elements of triplet hence we iterate through the slice
        for i in range(n - 2):

            l, r = i + 1, n - 1
            while l < r:
                x, y, z = nums[i], nums[l], nums[r]

                threeSum = x + y + z

                # found triplet
                if threeSum == 0:
                    res.add((x, y, z))

                    l += 1

                    while y != nums[l - 1]:
                        l += 1

                if threeSum > 0:
                    r -= 1
                    continue
                
                if threeSum < 0:
                    l += 1
                    continue
                
        return list(res)

