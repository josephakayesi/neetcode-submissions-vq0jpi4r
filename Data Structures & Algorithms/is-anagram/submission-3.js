class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
            if (s.length !== t.length) return false;

            const count = {};

            // Count characters in s
            for (let char of s) {
                count[char] = (count[char] || 0) + 1;
            }

            // Subtract characters using t
            for (let char of t) {
                if (!count[char]) return false; // either undefined or 0
                count[char]--;
            }

            return true;
        }
}
