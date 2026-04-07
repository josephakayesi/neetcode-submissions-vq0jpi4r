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

const rows = Array.from({ length: 9 }, () => new Set());
const columns = Array.from({ length: 9 }, () => new Set());
const squares = Array.from({ length: 9 }, () => new Set());

for (let row = 0; row < 9; row++) {
    for (let col = 0; col < 9; col++) {
        const val = board[row][col];
        if (val === '.') continue;

        const squareIndex = Math.floor(row / 3) * 3 + Math.floor(col / 3);

        if (
            rows[row].has(val) ||
            columns[col].has(val) ||
            squares[squareIndex].has(val)
        ) {
            return false;
        }

        rows[row].add(val);
        columns[col].add(val);
        squares[squareIndex].add(val);
    }
}
return true;

        // const traverseRows = () => {
        //     for(let i = 0; i < 9; i++){
        //         let set = new Set()

        //         for(let j = 0; j < gridWidth; j++){
        //             const value = board[i][j]

        //             if(value == '.'){
        //                continue
        //             }

        //             if (set.has(value)){
        //                 return false
        //             }

        //             set.add(value)
        //         }

        //     }

        //     return true
        // }

        // const traverseColumns = () => {
        //     for(let i = 0; i < gridLength; i++){
        //         let set = new Set()

        //         for(let j = 0; j < gridWidth; j++){
        //             const value = board[j][i]

        //             if(value == '.'){
        //                continue
        //             }

        //             if (set.has(value)){
        //                 return false
        //             }

        //             set.add(value)
        //         }

        //     }

        //     return true

        // }

        // const traverseSubBoxes = () => {
        //     let map = {}

        //     for (let i = 0; i < 9; i++){
        //         for (let j = 0; j < 9; j++){
        //             const x = Math.floor(i / 3)
        //             const y = Math.floor(j / 3)

        //             let key = [x, y]

        //             if(!map[key]){
        //                 map[key] = new Set() 
        //             } 

        //             const value = board[i][j]

        //             if(value == '.'){
        //                 continue
        //             }


        //             if(map[key].has(value)){
        //                 return false
        //             }

        //             map[key].add(value)
        //         }
        //     }

        //     return true
        // }

        // return traverseRows() && traverseSubBoxes() && traverseColumns()

        // }

}
}
