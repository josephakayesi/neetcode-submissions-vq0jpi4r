func twoSum(nums []int, target int) []int {
    /*
		- Keep a hash of the form { value: index }
		- For each value in the nums array check if the difference exists
		- If it exists return the two indices
	*/

	seen := map[int]int{}

	for i, num := range nums {
		difference := target - num

		if j, ok := seen[difference]; ok {
			return []int{j, i}
		}

		seen[num] = i
	}

	return nil
}