class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freqMap = new Map();

        // Step 1: Count frequencies
        for (const num of nums) {
            freqMap.set(num, (freqMap.get(num) || 0) + 1);
        }

        // Step 2: Build buckets — index = frequency
        const buckets = Array(nums.length + 1).fill(null).map(() => []);

        for (const [num, freq] of freqMap.entries()) {
            buckets[freq].push(num);
        }

        // Step 3: Collect k most frequent from buckets
        const result = [];
        for (let i = buckets.length - 1; i >= 0 && result.length < k; i--) {
            if (buckets[i].length) result.push(...buckets[i])

            if (result.length >= k) {
                return result.slice(0, k)
            }
        }

        return result.slice(0, k); 
    }
}











































