class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(key for key, val in Counter(nums).most_common(k))