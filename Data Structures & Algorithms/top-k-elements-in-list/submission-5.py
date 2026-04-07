class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Intuition:
        - Use a counter and return the top k most frequent
        """

        freq = Counter(nums)

        return [val for val, _ in freq.most_common(k)]
        