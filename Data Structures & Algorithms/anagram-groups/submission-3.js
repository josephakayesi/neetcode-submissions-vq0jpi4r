class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
        groupAnagrams(strs) {
            const groups = new Map()

            for (let str of strs){
                let count = new Uint8Array(26)

                for(const char of str){
                    count[char.toLowerCase().charCodeAt(0) - 97]++
                }

                const key = count.join('~')

                if(!groups.has(key)) {
                    groups.set(key, [])
                }

                groups.get(key).push(str)
            }


        return Array.from(groups.values())
    }
}
