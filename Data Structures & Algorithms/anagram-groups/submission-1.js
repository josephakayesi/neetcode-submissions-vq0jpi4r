class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        // Iterate through the array
        // For each string calculate the ascii sum and then add to a map {asciiSum: [index of string]}
        //

        const wordMap = {}
        const groupAnagrams = []
        
        for(const word of strs){
            const sortedWord = word.split("").sort().join("")

            if(!wordMap[sortedWord]){
                wordMap[sortedWord] = []
            }

            wordMap[sortedWord].push(word)
        }

        console.log("wordMap: ", wordMap)
        for(const values of Object.values(wordMap)){
            groupAnagrams.push(values)
        }

        return groupAnagrams

    }
}
