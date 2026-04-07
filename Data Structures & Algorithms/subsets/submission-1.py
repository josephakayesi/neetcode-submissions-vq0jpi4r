class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            if index == len(nums):
                res.append(path[:])
                return

            # Make decision to choose current number
            path.append(nums[index])
            dfs(index + 1, path)

            # Make decision to not choose current number
            path.pop()
            dfs(index + 1, path)

        dfs(0, [])
        return res