class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        if (s.length <= 1) return s;

        let longest = "";

        const expandAroundCenter = (left, right) => {
            while (left >= 0 && right < s.length && s[left] === s[right]) {
                left--;
                right++;
            }
            // slice from (left + 1) to (right - 1), inclusive
            return s.slice(left + 1, right);
        };

        for (let i = 0; i < s.length; i++) {
            // Odd-length palindrome
            const odd = expandAroundCenter(i, i);
            if (odd.length > longest.length) longest = odd;

            // Even-length palindrome
            const even = expandAroundCenter(i, i + 1);
            if (even.length > longest.length) longest = even;
        }

        return longest;
    }
}
