class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let numsSet = new Set(nums)
        let longestSequence = 0

        for(const num of nums){
            if(!numsSet.has(num-1)){
                let currentSequence = num
                let currentSequenceLength = 0

                while(numsSet.has(currentSequence)){
                    currentSequence += 1
                    currentSequenceLength += 1
                }

                longestSequence = Math.max(currentSequenceLength, longestSequence)
            }
        }

        return longestSequence
    }
}