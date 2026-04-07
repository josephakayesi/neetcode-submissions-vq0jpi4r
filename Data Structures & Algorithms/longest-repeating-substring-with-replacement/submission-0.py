class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: s = "ABAB", k = 2
        Output: 4  

        Thought process:
        - Count of the characters
        - Keep a left and right pointer for sliding window.
        - Iterate through my string
        - Find my window legnth and the max frequency
        - At each window check:
            - WindowLenght - MaxFrequency == The max number of characters I need to change to get my longest repeating character 

            LRCN <= k

        - Update longest = max(longest, window_length)
        - Return longest

        Input: s = "ABAB", k = 2
                    l
                         r
        freq = {
            A: 2,
            B: 2
        } 

        longest = 4
        """

        freq = {}
        l = r = 0
        longest = 0

        while r < len(s):
            window = (r - l) + 1
            freq[s[r]] = 1 + freq.get(s[r], 0)

            max_freq = max(freq.values())

            if window - max_freq <= k:
                longest = max(longest, window)
                r += 1
            else:
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1
                r += 1

        return longest
     