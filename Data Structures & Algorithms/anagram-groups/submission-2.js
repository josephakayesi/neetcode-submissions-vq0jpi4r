class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    // groupAnagrams(strs) {
    //     const wordMap = {}
    //     const groupAnagrams = []
        
    //     for(const word of strs){
    //         const sortedWord = word.split("").sort().join("")

    //         if(!wordMap[sortedWord]){
    //             wordMap[sortedWord] = []
    //         }

    //         wordMap[sortedWord].push(word)
    //     }

    //     for(const values of Object.values(wordMap)){
    //         groupAnagrams.push(values)
    //     }

    //     return groupAnagrams

    // }

        groupAnagrams(strs) {
        const wordMap = new Map();

        for (const word of strs) {
            // Create a frequency key of characters 'a' to 'z'
            const count = new Array(26).fill(0);
            for (const char of word) {
                count[char.charCodeAt(0) - 97]++;
            }
            const key = count.join('#'); // '#' as separator to avoid ambiguity

            if (!wordMap.has(key)) {
                wordMap.set(key, []);
            }

            wordMap.get(key).push(word);
        }

        return Array.from(wordMap.values());
    }
}
