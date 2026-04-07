class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {

        // This requires a DFS approach. 

        // Possible solution -
        /**
         * Go through each row;
         * Goo through each column
         * Then go through each subBox
         * 
         * 
         */

        let gridLength = 9 
        let gridWidth = 9

        const traverseRows = () => {
            for(let i = 0; i < 9; i++){
                let set = new Set()

                for(let j = 0; j < gridWidth; j++){
                    const value = board[i][j]

                    if(value == '.'){
                       continue
                    }

                    if (set.has(value)){
                        return false
                    }

                    set.add(value)
                }

            }

            return true
        }

        const traverseColumns = () => {
            for(let i = 0; i < gridLength; i++){
                let set = new Set()

                for(let j = 0; j < gridWidth; j++){
                    const value = board[j][i]

                    if(value == '.'){
                       continue
                    }

                    if (set.has(value)){
                        return false
                    }

                    set.add(value)
                }

            }

            return true

        }

        const traverseSubBoxes = () => {
            let map = {}

            for (let i = 0; i < 9; i++){
                for (let j = 0; j < 9; j++){
                    const x = Math.floor(i / 3)
                    const y = Math.floor(j / 3)

                    let key = [x, y]

                    if(!map[key]){
                        map[key] = new Set() 
                    } 

                    const value = board[i][j]

                    if(value == '.'){
                        continue
                    }


                    if(map[key].has(value)){
                        return false
                    }

                    map[key].add(value)
                }
            }

            return true
        }

        return traverseRows() && traverseSubBoxes() && traverseColumns()

        }

}
