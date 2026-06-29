class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        - Keep two pointers moving from opposite directions towards the center.
        - left and right pointer.
        - keep moving the pointers to the center whilst the character is a valid alphabet and equals each other.
        - If equal move both; if not equal return false.
        - If either left or right encounters invalid character move the pointers one step.
        """

        l, r = 0, len(s) - 1

        while l <= r:
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower():
                return False

            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1

        return True
