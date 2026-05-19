class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Assumptions:
        - There is guaranteed to be at least one triplet.

        Intuition:
        - I will sort the nums. 
        - I will start iterating through the values of nums; first with i and j. 
        - To find k; check if sum of (i + j + k) == 0;
        - If we find a valid triplet then we return triplet
        - Otherwise we move i and j forward by one and then continue with finding valid triplets. 
        - If no triplets return []

                    i  j
        nums = [-2, 0, 1, 1, 2]
                 a     b        c
        n = 6 

        triplets = [[-2, 0, 2]]
        """

        nums.sort()
        n = len(nums)
        triplets = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]

                if total == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                                   
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1

                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
 
        return triplets

        # for i in range(n - 2):
        #     a = nums[i]

        #     l = i + 1
        #     k = n - 1

        #     while j < k:
        #         b = nums[j]
        #         c = nums[k]

        #         total = a + b + c

        #         if total == 0:
        #             triplets.add((a, b, c))
        #             break
                
        #         if total < 0:
        #             j += 1
        #         else:
        #             k -= 1
        # return list(triplets)


        # while j < n - 1:
        #     a, b = nums[i], nums[j]

        #     for k in range(j + 1, n):
        #         c = nums[k]

        #         if a + b + c == 0:
        #             triplets.add((a, b, c))
            
        #     i += 1
        #     j += 1
        
        # return list(triplets)
