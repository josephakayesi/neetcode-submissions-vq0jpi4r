class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let stack = []
        const combinations = {
            '{}': true,
            '()': true,
            '[]': true
        }

        for (let char of s){
            if(!stack.length){
                stack.push(char)
                continue
            }

            let poppedItem = stack.pop() 
            let current = `${poppedItem}${char}`
            if(combinations[current]){
                continue
            }

            stack.push(poppedItem)
            stack.push(char)
        }

        return stack.length == 0
    }
}
