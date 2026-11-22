func hasDuplicate(nums []int) bool {
    /* 
		- Keep a hash of seen numbers
		- Iterate through the nums slice.
		- Check if the current number exists in seen
		- If exists return true otherwise keep iterating
		- Once you iterate the entire slice an no duplicate found, simply return false
	*/

	seen := map[int]struct{}{}

	for _, v := range nums {
		if _, ok := seen[v]; ok {
			return true
		}

		seen[v] = struct{}{}
	}

	return false
}
