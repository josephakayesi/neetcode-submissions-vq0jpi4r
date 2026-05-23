class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition:
        - Start at the root and check fo every possible combination that can be formed from nums
        - At each decision; you weither choose the current node or not. 
        - Find all combinations for each subset until you have exhausted your decision tree
        """

        res = [] 

        def dfs(index, path):
            if index >= len(nums):
                res.append(path.copy())
                return 

            # add node 
            path.append(nums[index])
            dfs(index + 1, path)

            # current node not included
            path.pop()

            dfs(index + 1, path)


        dfs(0, [])

        return res

