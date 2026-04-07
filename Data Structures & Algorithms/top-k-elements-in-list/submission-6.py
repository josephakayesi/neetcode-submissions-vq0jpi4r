# Using built-in counter 
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         """
#         Intuition:
#         - Use a counter and return the top k most frequent
#         """

#         freq = Counter(nums)

#         return [val for val, _ in freq.most_common(k)]
        
# Using bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)] 

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for key, c in count.items():
            freq[c].append(key)

        res = [] 

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res 
        
        

