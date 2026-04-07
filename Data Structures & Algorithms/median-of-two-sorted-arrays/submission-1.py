class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A, B = nums1, nums2
        m, n = len(A), len(B)

        # i is the split position in A, j in B
        # half is the total number of elements on the left side
        half = (m + n + 1) // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half - i

            Aleft  = float('-inf') if i == 0 else A[i - 1]
            Aright = float('inf')  if i == m else A[i]
            Bleft  = float('-inf') if j == 0 else B[j - 1]
            Bright = float('inf')  if j == n else B[j]

            if Aleft <= Bright and Bleft <= Aright:
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1