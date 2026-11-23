func twoSum(nums []int, target int) []int {
    /*
		- Keep a hash of the form { value: index }
		- For each value in the nums array check if the difference exists
		- If it exists return the two indices
	*/

	indices := map[int]int{}

	for i, v := range nums {
		difference := target - v

		if index, ok := indices[difference]; ok {
			return []int{index, i}
		}

		indices[v] = i
	}

	return []int{}
}
