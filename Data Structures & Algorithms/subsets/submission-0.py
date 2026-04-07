class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if index >= len(nums):
                res.append(path[:])
                return

            # Make decision to choose current number
            path.append(nums[index])
            backtrack(index + 1, path)

            # Make decision to not choose current number
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        return res