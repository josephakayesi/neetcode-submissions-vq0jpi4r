class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Intuition
        - We need to find all combinations of numbers that will sum to the target.
        - At each decision, we have a choice to choose an element, skip an element or rechoose the same element
        - When you decide to choose an element you need to check that the sum won't exceed the current subset(path) choice
        - The basecase is when the sum of the current choice exceeds the target 
        """


        res = []

        def dfs(index, path, curr_sum):
            if index >= len(nums) or curr_sum > target:
                return 

            if curr_sum == target:
                res.append(path.copy())
                return 

            path.append(nums[index])
            dfs(index, path, curr_sum + nums[index])
            path.pop()

            dfs(index + 1, path, curr_sum)


        dfs(0, [], 0)
        return res
        