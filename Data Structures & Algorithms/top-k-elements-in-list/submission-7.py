from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
        - Bucket approach
        - Keep a frequency map and keep track of the frequency of each
        - Iterate through the nums list and update the frequency
        - Iterate through the freq map and update the frequency in the bucket
        - Iterate through my bucket from right to left and then add the k most frequent elements from each bucket
        - Add the elements from right to left in the res and break when len == k
        - Return the result

        freq = {1: 3, 2: 2, 3: 1}

        bucket = [[], [3], [2], [1], [], [], []]
        res = [1, 2]

        - Use a counter variable initialized as a Counter
        - Then using `most_common(k)` helper method in Counter; return the top k most frequent elements


        Assumptions
        - If two elements are top k then return the first element from the left that is frequently occuring
        - For empty -> []
        - For null -> []

        Time complexity: O(n)
        Space complexity: O(n)

        counter = { 1: [3], 2: [2], 3: [1]}
        """

        counter = Counter(nums)
        return [k for k, v in counter.most_common(k)]